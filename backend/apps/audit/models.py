from django.db import models
from apps.emissions.models import EmissionRecord


class AuditLog(models.Model):

    ACTION_CHOICES = [
        ("APPROVED", "APPROVED"),
        ("FLAGGED", "FLAGGED"),
        ("LOCKED", "LOCKED"),
        ("UPDATED", "UPDATED"),
    ]

    record = models.ForeignKey(
        EmissionRecord,
        on_delete=models.CASCADE
    )

    action = models.CharField(max_length=50)

    performed_by = models.CharField(max_length=255)

    comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)