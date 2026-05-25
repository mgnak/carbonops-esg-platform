from django.shortcuts import render






# Create your views here.
# # api/views.py
# from rest_framework import viewsets, status, filters
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend
# from core.models import EmissionRecord, Company, DataSource
# from .serializers import (
#     EmissionRecordSerializer, 
#     CompanySerializer, 
#     DataSourceSerializer,
#     AuditLogSerializer
# )
# from django.shortcuts import get_object_or_404


# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer


# class DataSourceViewSet(viewsets.ModelViewSet):
#     queryset = DataSource.objects.all()
#     serializer_class = DataSourceSerializer


# class EmissionRecordViewSet(viewsets.ModelViewSet):
#     queryset = EmissionRecord.objects.all()
#     serializer_class = EmissionRecordSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
#     filterset_fields = ['company', 'source__name', 'status', 'scope']
#     search_fields = ['category', 'raw_file_name']
#     ordering_fields = ['record_date', 'created_at', 'normalized_amount']

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         # For now, allow all (later add company filtering)
#         return queryset

#     @action(detail=True, methods=['post'])
#     def approve(self, request, pk=None):
#         record = self.get_object()
#         record.status = 'approved'
#         record.reviewed_by = request.user
#         record.reviewed_at = timezone.now()  # import timezone from django.utils
#         record.save()

#         # Create audit log
#         AuditLog.objects.create(
#             record=record,
#             action='approved',
#             user=request.user,
#             details={"previous_status": "pending" if record.status == 'approved' else record.status}
#         )
#         return Response({"status": "approved"})

#     @action(detail=True, methods=['post'])
#     def reject(self, request, pk=None):
#         record = self.get_object()
#         record.status = 'rejected'
#         record.reviewed_by = request.user
#         record.reviewed_at = timezone.now()
#         record.flagged_reason = request.data.get('reason', '')
#         record.save()

#         AuditLog.objects.create(
#             record=record,
#             action='rejected',
#             user=request.user,
#             details={"reason": record.flagged_reason}
#         )
#         return Response({"status": "rejected"})

#     @action(detail=True, methods=['post'])
#     def mark_suspicious(self, request, pk=None):
#         record = self.get_object()
#         record.status = 'suspicious'
#         record.flagged_reason = request.data.get('reason', 'Manually flagged')
#         record.save()
#         return Response({"status": "suspicious"})







from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from core.models import EmissionRecord, AuditLog


class EmissionRecordViewSet(viewsets.ModelViewSet):
    queryset = EmissionRecord.objects.all()
    serializer_class = EmissionRecordSerializer
    # Use your serializer from before

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        record = self.get_object()
        record.status = 'approved'
        record.reviewed_by = request.user if request.user.is_authenticated else None
        record.reviewed_at = timezone.now()
        record.save()

        AuditLog.objects.create(
            record=record,
            action='approved',
            user=request.user if request.user.is_authenticated else None,
            details={"status": "approved"}
        )
        return Response({"status": "approved"})