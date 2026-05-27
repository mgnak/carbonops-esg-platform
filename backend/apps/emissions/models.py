from django.db import models
from apps.tenants.models import Tenant
from apps.ingestion.models import SourceLog


class EmissionRecord(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "PENDING"),
        ("APPROVED", "APPROVED"),
        ("FLAGGED", "FLAGGED"),
        ("LOCKED", "LOCKED"),
    ]

    SCOPE_CHOICES = [
        ("SCOPE_1", "SCOPE_1"),
        ("SCOPE_2", "SCOPE_2"),
        ("SCOPE_3", "SCOPE_3"),
    ]

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    source_log = models.ForeignKey(
        SourceLog,
        on_delete=models.PROTECT
    )

    scope = models.CharField(
        max_length=20,
        choices=SCOPE_CHOICES
    )

    activity_type = models.CharField(max_length=100)

    raw_value = models.FloatField()
    raw_unit = models.CharField(max_length=50)

    normalized_value = models.FloatField()
    normalized_unit = models.CharField(max_length=50)

    co2e_kg = models.FloatField()

    activity_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    is_manually_edited = models.BooleanField(default=False)

    reviewer_notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} - {self.co2e_kg} kgCO2e"