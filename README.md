# LogAnalyticsIngestionExample

This repository contains examples of Log Analytics Ingestion using Python.

## Files in this repository:

### 1. `IngestToLawDCR.py`

This script demonstrates how to use the Logs Ingestion API in Azure Monitor to send external data to a Log Analytics workspace with a REST API and Data Collection Rule (DCR).

**Reference**:  
[Azure Monitor Logs Ingestion Tutorial](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/tutorial-logs-ingestion-portal)

---

### 2. `IngestToLaw.py` (HTTP Data Collector API - Deprecated)

This script shows how to use the **HTTP Data Collector API** to send log data to Azure Monitor from a REST API client.

**Reference**:  
[HTTP Data Collector API (Deprecated)](https://learn.microsoft.com/en-us/previous-versions/azure/azure-monitor/logs/data-collector-api?tabs=powershell)

---

## Requirements

- Python 3.x
- Azure subscription
- Required Python libraries (e.g., `requests`)


