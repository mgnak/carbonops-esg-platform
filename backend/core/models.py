from django.db import models

from django.contrib.auth.models import User
import uuid

class Company(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.name

class DataSource(models.Model):
    SOURCE_CHOICES = [
        ('sap_fuel', 'SAP Fuel & Procurement'),
        ('utility_electricity', 'Utility Electricity'),
        ('corporate_travel', 'Corporate Travel'),
    ]
    name = models.CharField(max_length=50, choices=SOURCE_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class EmissionRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    source = models.ForeignKey(DataSource, on_delete=models.PROTECT)
    
    # Common normalized fields
    record_date = models.DateField()
    scope = models.CharField(max_length=10, choices=[('1','1'), ('2','2'), ('3','3')])
    category = models.CharField(max_length=100)  # e.g., "Fuel - Diesel", "Electricity", "Flight"
    
    # Activity data (raw + normalized)
    raw_amount = models.DecimalField(max_digits=15, decimal_places=4)
    raw_unit = models.CharField(max_length=50)
    normalized_amount = models.DecimalField(max_digits=15, decimal_places=4)  # in kgCO2e or base unit
    normalized_unit = models.CharField(max_length=50, default='kgCO2e')
    
    # Metadata
    original_data = models.JSONField()  # Store raw row for audit
    raw_file_name = models.CharField(max_length=255, null=True)
    
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending Review'),
        ('suspicious', 'Suspicious'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='pending')
    
    flagged_reason = models.TextField(blank=True)
    reviewed_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='reviewed_records')
    reviewed_at = models.DateTimeField(null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

# Audit Trail
class AuditLog(models.Model):
    record = models.ForeignKey(EmissionRecord, on_delete=models.CASCADE, related_name='audit_logs')
    action = models.CharField(max_length=50)  # uploaded, status_changed, edited
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.JSONField()