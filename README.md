# CarbonOps ESG Platform

## Overview

CarbonOps is a full-stack ESG emissions ingestion and analyst review platform designed to simulate enterprise carbon accounting workflows.

The platform ingests emissions-related operational data from multiple enterprise systems, normalizes units into a common representation, calculates CO₂e emissions, detects suspicious records, and introduces a human-in-the-loop analyst review process before records are locked for audit.

This project was developed as part of a technical assessment focused on ESG data engineering, auditability, and workflow design.

---

# Problem Statement

Enterprise ESG data is fragmented across multiple operational systems such as:

* SAP fuel/procurement exports
* Utility provider CSVs
* Corporate travel platforms

These systems:

* export inconsistent formats
* use different units
* contain missing or suspicious data
* lack audit traceability

The goal of this platform is to centralize ingestion, normalization, validation, and analyst review into a unified ESG workflow.

---

# Core Workflow

```text
Upload Data
    ↓
Normalize Units
    ↓
Calculate CO₂e
    ↓
Detect Suspicious Rows
    ↓
Analyst Review
    ↓
Approve / Flag
    ↓
Lock for Audit
```

---

# Key Features

## Data Ingestion

Supports ingestion from:

* SAP flat file exports
* Utility CSV uploads
* Corporate travel datasets

---

## Emissions Normalization

Converts inconsistent units into normalized formats while preserving original values.

Examples:

* gallons → liters
* miles → kilometers
* kWh normalization

---

## CO₂e Calculation

Uses emission factor mappings to calculate:

* Scope 1 emissions
* Scope 2 emissions
* Scope 3 emissions

---

## Suspicious Data Detection

Automatically flags records containing:

* unusually high activity values
* inconsistent units
* malformed dates
* invalid conversions

---

## Analyst Review Workflow

Human analysts can:

* approve rows
* flag records
* manually inspect anomalies
* lock approved records for audit

---

## Auditability

Every ingestion event stores:

* original file source
* upload timestamp
* checksum
* uploader identity
* ingestion status

This preserves traceability throughout the ESG reporting lifecycle.

---

# Tech Stack

## Backend

* Python 3.12
* Django 5
* Django REST Framework
* Pandas
* SQLite (local development)
* PostgreSQL (deployment-ready)

---

## Frontend

* React
* Vite
* Tailwind CSS
* Axios

---

## Deployment

* Backend → Render
* Frontend → Vercel

---

# Folder Structure

```text
CarbonOps/
│
├── backend/
│   ├── apps/
│   ├── config/
│   ├── requirements/
│   └── manage.py
│
├── frontend/
│   ├── src/
│   └── package.json
│
├── README.md
├── MODEL.md
├── DECISIONS.md
└── ARCHITECTURE.md
```

---

# Running Locally

## Backend

```powershell
cd backend

py -3.12 -m venv venv

.\venv\Scripts\Activate

pip install -r requirements/base.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

## Frontend

```powershell
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

# API Endpoints

## Upload APIs

```text
/api/ingestion/sap/upload/
/api/ingestion/utility/upload/
/api/ingestion/travel/upload/
```

---

## Review APIs

```text
/api/review/pending/
/api/review/approve/<id>/
/api/review/flag/<id>/
```

---

# Sample CSV

```csv
Volume,Unit,Fuel_Type,Date
200,liters,Diesel,2025-01-01
500,gallons,Petrol,2025-01-02
```

---

# Future Improvements

* Asynchronous ingestion pipelines
* Row-level edit history
* Multi-tenant authentication
* Advanced anomaly detection
* Bulk review actions
* Emission factor versioning
* S3 object storage
* Role-based permissions

---

# Design Priorities

The project prioritizes:

1. Auditability
2. Traceability
3. Data normalization integrity
4. Human review workflows
5. Clear data modeling

over visual complexity or advanced UI animation.

---

# Author

Meghana K
