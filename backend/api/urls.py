# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import CompanyViewSet, DataSourceViewSet, EmissionRecordViewSet

# router = DefaultRouter()
# router.register(r'companies', CompanyViewSet)
# router.register(r'datasources', DataSourceViewSet)
# router.register(r'emission-records', EmissionRecordViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]




# ingestion/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .services import process_file_upload
from core.models import EmissionRecord

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file = request.FILES.get('file')
        source_type = request.data.get('source_type')  # sap_fuel, utility_electricity, corporate_travel

        if not file or not source_type:
            return Response({"error": "File and source_type are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            count = process_file_upload(file, source_type)
            return Response({
                "message": f"Successfully processed {count} records",
                "source": source_type,
                "records_created": count
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)