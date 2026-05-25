from django.db import models
from django.contrib.auth.models import User
import uuid

class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DataSource(models.Model):
    SOURCE_CHOICES = [
        ('sap_fuel', 'SAP Fuel & Procurement'),
        ('utility_electricity', 'Utility Electricity'),
        ('corporate_travel', 'Corporate Travel'),
    ]
    name = models.CharField(max_length=50, choices=SOURCE_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='data_sources')

    class Meta:
        unique_together = ('name', 'company')

    def __str__(self):
        return self.name


class EmissionRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    source = models.ForeignKey(DataSource, on_delete=models.PROTECT)
    
    record_date = models.DateField()
    scope = models.CharField(max_length=10, choices=[('1', 'Scope 1'), ('2', 'Scope 2'), ('3', 'Scope 3')])
    category = models.CharField(max_length=100)
    
    raw_amount = models.DecimalField(max_digits=15, decimal_places=4)
    raw_unit = models.CharField(max_length=50)
    normalized_amount = models.DecimalField(max_digits=15, decimal_places=4)
    normalized_unit = models.CharField(max_length=50, default='kgCO2e')
    
    original_data = models.TextField(default='{}')
    raw_file_name = models.CharField(max_length=255, blank=True, null=True)
    
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending Review'),
        ('suspicious', 'Suspicious'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='pending')
    
    flagged_reason = models.TextField(blank=True)
    reviewed_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='reviewed_records')
    reviewed_at = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


class AuditLog(models.Model):
    record = models.ForeignKey(EmissionRecord, on_delete=models.CASCADE, related_name='audit_logs')
    action = models.CharField(max_length=50)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(default='{}')

    class Meta:
        ordering = ['-timestamp']