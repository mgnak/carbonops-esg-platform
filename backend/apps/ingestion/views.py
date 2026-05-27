import hashlib
import pandas as pd

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from apps.tenants.models import Tenant
from apps.ingestion.models import SourceLog
from apps.emissions.models import EmissionRecord

from .utils import (
    normalize_value,
    calculate_co2e
)


@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def upload_sap_file(request):

    if 'file' not in request.FILES:
        return Response({
            "error": "No file uploaded"
        }, status=400)

    file = request.FILES['file']

    tenant = Tenant.objects.first()

    if not tenant:
        return Response({
            "error": "No tenant found"
        }, status=400)

    checksum = hashlib.md5(
        file.read()
    ).hexdigest()

    file.seek(0)

    source_log = SourceLog.objects.create(
        tenant=tenant,
        source_type="SAP",
        file_name=file.name,
        uploaded_by="admin",
        checksum=checksum,
        ingestion_status="PROCESSING"
    )

    try:

        df = pd.read_csv(file)

        for _, row in df.iterrows():

            normalized = normalize_value(
                row['Volume'],
                row['Unit']
            )

            co2e = calculate_co2e(
                row['Fuel_Type'],
                normalized
            )

            EmissionRecord.objects.create(
                tenant=tenant,
                source_log=source_log,
                scope="SCOPE_1",
                activity_type=row['Fuel_Type'],
                raw_value=row['Volume'],
                raw_unit=row['Unit'],
                normalized_value=normalized,
                normalized_unit="STANDARD",
                co2e_kg=co2e,
                activity_date=row['Date']
            )

        source_log.ingestion_status = "COMPLETED"
        source_log.save()

        return Response({
            "message": "SAP file uploaded successfully"
        })

    except Exception as e:

        source_log.ingestion_status = "FAILED"
        source_log.save()

        return Response({
            "error": str(e)
        }, status=500)