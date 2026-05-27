from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.emissions.models import EmissionRecord
from apps.audit.models import AuditLog


@api_view(["POST"])
def approve_record(request, pk):

    record = EmissionRecord.objects.get(id=pk)

    record.status = "APPROVED"
    record.save()

    AuditLog.objects.create(
        record=record,
        action="APPROVED",
        performed_by="analyst"
    )

    return Response({"message": "Approved"})


@api_view(["POST"])
def flag_record(request, pk):

    record = EmissionRecord.objects.get(id=pk)

    record.status = "FLAGGED"
    record.save()

    AuditLog.objects.create(
        record=record,
        action="FLAGGED",
        performed_by="analyst"
    )

    return Response({"message": "Flagged"})


@api_view(["POST"])
def lock_record(request, pk):

    record = EmissionRecord.objects.get(id=pk)

    record.status = "LOCKED"
    record.save()

    AuditLog.objects.create(
        record=record,
        action="LOCKED",
        performed_by="analyst"
    )

    return Response({"message": "Locked"})