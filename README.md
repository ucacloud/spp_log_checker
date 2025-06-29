# SPP Log Checker

A Python script that scans system log files for compliance-related events such as failed login attempts and expired certificates.

## 🔍 What It Does

- Parses a single `.log` file from the `logs/` folder
- Tracks and summarizes:
  - Failed login attempts
  - Expired security certificates
  - Users with 3+ failed login attempts (triggers an alert)
- Generates a timestamped compliance report in `/reports`
- Moves processed logs into `/log_archive`
- Deletes archived logs older than 10 minutes (for testing)

## 🛠 How to Use

1. Drop **one** `.log` file into the `/logs/` folder
2. Run `spp_log_checker.py`
3. Read the output in the console and the generated report
4. Your log will be moved to `/log_archive`
5. Any archived logs older than 10 minutes will be auto-deleted

## 📂 Folder Structure

- spp_log_checker/
- ├── logs/
- ├── log_archive/
- ├── reports/
- ├── spp_log_checker.py
- └── README.md

## 🧪 Example Log Entry Format

- 2025-06-27 00:01:12 - LOGIN - user1 - FAILED 
- 2025-06-27 00:11:50 - CERT - certB - expired


## ✅ Requirements

- Python 3.x
- No external dependencies — uses only built-in libraries

---
