# api/serializers.py
from rest_framework import serializers
from core.models import EmissionRecord, Company, DataSource, AuditLog

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = ['id', 'name', 'company']


class EmissionRecordSerializer(serializers.ModelSerializer):
    source_name = serializers.CharField(source='source.name', read_only=True)
    reviewed_by_username = serializers.CharField(source='reviewed_by.username', read_only=True)

    class Meta:
        model = EmissionRecord
        fields = '__all__'
        # [
        #     'id', 'company', 'source', 'source_name',
        #     'record_date', 'scope', 'category',
        #     'raw_amount', 'raw_unit', 'normalized_amount', 'normalized_unit',
        #     'original_data', 'raw_file_name',
        #     'status', 'flagged_reason',
        #     'reviewed_by', 'reviewed_by_username', 'reviewed_at',
        #     'created_at', 'updated_at'
        # ]
        read_only_fields = ['normalized_amount', 'normalized_unit', 'reviewed_by', 'reviewed_at']


class EmissionRecordCreateSerializer(serializers.ModelSerializer):
    """Used for internal creation (ingestion)"""
    class Meta:
        model = EmissionRecord
        fields = [
            'company', 'source', 'record_date', 'scope', 'category',
            'raw_amount', 'raw_unit', 'normalized_amount', 'normalized_unit',
            'original_data', 'raw_file_name'
        ]


class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = ['id', 'action', 'user', 'timestamp', 'details']