from django.db import models
from apps.tenants.models import Tenant


class SourceLog(models.Model):

    SOURCE_CHOICES = [
        ("SAP", "SAP"),
        ("UTILITY", "UTILITY"),
        ("TRAVEL", "TRAVEL"),
    ]

    STATUS_CHOICES = [
        ("PROCESSING", "PROCESSING"),
        ("COMPLETED", "COMPLETED"),
        ("FAILED", "FAILED"),
    ]

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    source_type = models.CharField(
        max_length=50,
        choices=SOURCE_CHOICES
    )

    file_name = models.CharField(max_length=255)

    uploaded_by = models.CharField(max_length=255)

    ingestion_status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="PROCESSING"
    )

    checksum = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source_type} - {self.file_name}"