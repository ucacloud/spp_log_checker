import os

log_file_path = os.path.join("logs", "system_log_2025-06-25.log")

if os.path.exists(log_file_path):
    print(f"Reading log file: {log_file_path}")

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            line = line.strip()
            parts = line.split(" - ")

            if len(parts) >= 4:
                date_time = parts[0]
                event_type = parts[1]
                subject = parts [2]
                status = parts[3]

                print(f"Event: {event_type}, Subject: {subject}, Status: {status}")
            else:
                print("Skipping line: not in expected format")

else:
    print("Log file not found.")