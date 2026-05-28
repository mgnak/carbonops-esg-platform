# MODEL.md

# Data Model Design

## Overview

The CarbonOps data model is designed around four primary concerns:

1. Multi-tenancy
2. Auditability
3. Data normalization
4. Human review workflows

The schema intentionally preserves both original source data and normalized ESG reporting data to maintain traceability.

---

# Core Design Philosophy

The system treats uploaded enterprise data as:

* imperfect
* heterogeneous
* potentially inconsistent
* audit-sensitive

For that reason, the platform never overwrites source values after ingestion.

Instead:

* raw values are preserved
* normalized values are stored separately
* review actions are explicitly tracked

This ensures ESG calculations remain explainable and auditable.

---

# Primary Entities

## Tenant

Represents an organization using the platform.

### Purpose

Supports multi-tenant isolation where each organization's:

* uploads
* emissions records
* review workflows
* audit history

remain logically separated.

### Fields

| Field      | Purpose                   |
| ---------- | ------------------------- |
| name       | Organization name         |
| industry   | Industry classification   |
| created_at | Tenant creation timestamp |

---

# SourceLog

Tracks ingestion events.

### Purpose

Provides full ingestion traceability.

Each uploaded file creates a SourceLog entry containing:

* source system
* upload timestamp
* checksum
* uploader identity
* processing status

This enables:

* ingestion auditing
* duplicate detection
* operational debugging

### Why Separate SourceLog?

Separating ingestion metadata from emissions rows avoids duplication and allows many emissions records to reference a single ingestion source.

---

# EmissionRecord

Represents normalized ESG activity data.

This is the central analytical entity in the system.

---

# Raw vs Normalized Values

The model intentionally stores both:

| Type       | Example       |
| ---------- | ------------- |
| Raw        | 500 gallons   |
| Normalized | 1892.5 liters |

This separation was critical for several reasons:

## 1. Auditability

Auditors must verify:

* original uploaded value
* conversion logic
* normalized result

without losing source context.

---

## 2. Reprocessing Flexibility

If emission factor standards change later:

* normalized values can be recalculated
* original source data remains intact

---

## 3. Error Investigation

Analysts can compare:

* uploaded values
* converted values
* suspicious records

during manual review.

---

# Scope Classification

Each emissions row stores:

* Scope 1
* Scope 2
* Scope 3

explicitly.

This enables:

* downstream reporting
* dashboard aggregation
* ESG categorization
* audit segmentation

---

# Suspicious Flagging

The model includes a boolean suspicious flag.

### Purpose

Supports human-in-the-loop workflows.

The platform automatically flags:

* abnormal values
* unexpected unit conversions
* malformed uploads

before analyst approval.

This prevents fully automated acceptance of potentially incorrect ESG disclosures.

---

# Status Workflow

Emission records progress through states:

```text
PENDING
    ↓
APPROVED / FLAGGED
    ↓
LOCKED
```

---

# Why Statuses Exist

This reflects real-world ESG operational workflows where:

* analysts validate calculations
* auditors require locked historical records
* approved records should become immutable

---

# Why Locking Matters

Locked records:

* should not be editable
* represent finalized disclosures
* support audit integrity

This mirrors financial reporting principles.

---

# Multi-Tenancy Strategy

Tenant relationships are enforced using foreign keys.

Every primary entity references:

* Tenant

This prevents:

* cross-client data leakage
* mixed reporting contexts
* shared audit histories

---

# Why SQLite Initially?

SQLite was chosen for:

* rapid local development
* simplified onboarding
* zero infrastructure overhead

The schema is intentionally PostgreSQL-compatible for deployment migration later.

---

# Why Django ORM?

Django ORM was selected because it provides:

* rapid schema iteration
* migration management
* admin tooling
* relational consistency
* clean API integration

This accelerated development while preserving maintainability.

---

# Tradeoffs

## Simplicity vs Completeness

The current schema intentionally simplifies:

* emission factor versioning
* hierarchical organizations
* temporal factor snapshots

to prioritize:

* clarity
* explainability
* implementation speed

within the assignment timeframe.

---

# Future Extensions

Potential future additions include:

* versioned emission factors
* row-level change history
* immutable audit snapshots
* asynchronous ingestion jobs
* role-based access control
* approval chains
* tenant-specific unit mappings

---

# Final Design Goal

The data model prioritizes:

* explainability
* audit traceability
* workflow integrity
* normalization transparency

over aggressive optimization or premature complexity.
