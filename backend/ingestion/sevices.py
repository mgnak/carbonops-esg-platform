# ingestion/services.py
import pandas as pd
from decimal import Decimal
from django.utils import timezone
from core.models import EmissionRecord, DataSource, Company, AuditLog

def get_or_create_company(name="Test Company"):
    company, _ = Company.objects.get_or_create(name=name)
    return company

def get_or_create_source(company, source_name):
    source, _ = DataSource.objects.get_or_create(
        name=source_name, 
        company=company
    )
    return source

def normalize_fuel(row):
    try:
        amount = Decimal(row.get('amount', 0))
        unit = str(row.get('unit', '')).lower()
        if unit in ['l', 'liter', 'liters']:
            factor = Decimal('2.68')  # Diesel example
        elif unit in ['gal', 'gallon']:
            factor = Decimal('10.15')
        else:
            factor = Decimal('1')
        return amount * factor, 'kgCO2e'
    except:
        return Decimal('0'), 'kgCO2e'

def process_file_upload(file, source_type, company_name="Test Company"):
    company = get_or_create_company(company_name)
    source = get_or_create_source(company, source_type)
    
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)
    
    records = []
    for _, row in df.iterrows():
        try:
            if source_type == 'sap_fuel':
                norm_amount, norm_unit = normalize_fuel(row)
                record = EmissionRecord(
                    company=company,
                    source=source,
                    record_date=pd.to_datetime(row.get('date')).date(),
                    scope='1',
                    category=f"Fuel - {row.get('fuel_type', 'Unknown')}",
                    raw_amount=row.get('amount', 0),
                    raw_unit=row.get('unit', 'unknown'),
                    normalized_amount=norm_amount,
                    normalized_unit=norm_unit,
                    original_data=str(row.to_dict()),
                    raw_file_name=file.name,
                    status='pending'
                )
            # Add more for other sources later
            records.append(record)
        except Exception as e:
            print(f"Error processing row: {e}")
    
    created = EmissionRecord.objects.bulk_create(records)
    return len(created)