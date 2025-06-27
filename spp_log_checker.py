import os

log_file_path = os.path.join("logs", "system_log_2025-06-25.log")

if os.path.exists(log_file_path):
    print(f"Reading log file: {log_file_path}")

    failed_login_counts = {}
    expired_certs = []

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            line = line.strip()
            parts = line.split(" - ")

            if len(parts) >= 4:
                date_time = parts[0]
                event_type = parts[1]
                subject = parts[2]
                status = parts[3]

                if event_type == "LOGIN" and status == "FAILED":
                    if subject not in failed_login_counts:
                        failed_login_counts[subject] = 1
                    else:
                        failed_login_counts[subject] += 1

                elif event_type == "CERT" and status.lower() == "expired":
                    expired_certs.append(subject)

    print("\n=== Compliance Summary ===")

    if failed_login_counts:
        print("Failed Login Attempts:")
        for user, count in failed_login_counts.items():
            print(f" - {user}: {count} failed attempt(s)")
    else:
        print("No failed logins found.")

    if expired_certs:
         print("\nExpired Certificates:")
         for cert in expired_certs:
                    print(f" - {cert}")

    else:
         print("\nNo expired certificates found.")

else:
    print("Log file not found.")
