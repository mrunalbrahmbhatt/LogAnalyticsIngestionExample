# LogAnalyticsIngestionExample

This repository contains examples of Log Analytics Ingestion using Python.

## Files in this repository:

### 1. `IngestToLawDCR.py`

This script demonstrates how to use the Logs Ingestion API in Azure Monitor to send external data to a Log Analytics workspace with a REST API and Data Collection Rule (DCR).

**Reference**:  
[Azure Monitor Logs Ingestion Tutorial](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/tutorial-logs-ingestion-portal)

---

### 2. `IngestToLaw.py` (HTTP Data Collector API - Deprecated)

This script shows how to use the **HTTP Data Collector API** to send log data to Azure Monitor/Log Analytics workspace from a REST API client.

**Reference**:  
[HTTP Data Collector API (Deprecated)](https://learn.microsoft.com/en-us/previous-versions/azure/azure-monitor/logs/data-collector-api?tabs=powershell)

---

## Requirements

- Python 3.x
- Azure subscription
- Required Python libraries (e.g., `requests`)


## Disclaimer

This repository is provided **as-is**, without any warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, or non-infringement. The authors are not responsible for any damages or issues arising from the use of this code, including but not limited to direct, indirect, incidental, special, exemplary, or consequential damages, or loss of data or profits.

By using this repository, you agree to do so at your own risk. The authors make no representations or guarantees about the functionality, accuracy, or completeness of the code, and you are responsible for ensuring the code works as intended in your environment.

---

## License

This repository is licensed under the **MIT License**. You are free to use, modify, and distribute this code, provided that you include the original copyright and license notice in any copies of the code that you distribute.


