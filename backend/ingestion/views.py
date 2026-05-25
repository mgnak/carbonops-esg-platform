# ingestion/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .services import process_file_upload

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file = request.FILES.get('file')
        source_type = request.data.get('source_type')

        if not file or not source_type:
            return Response({"error": "File and source_type are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            count = process_file_upload(file, source_type)
            return Response({
                "message": f"Successfully processed {count} records from {source_type}",
                "records_created": count
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)