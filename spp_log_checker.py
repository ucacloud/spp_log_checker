import os
import shutil
import time
from datetime import datetime

logs_folder = "logs"
archive_folder = "log_archive"
log_files = [f for f in os.listdir(logs_folder) if f.endswith(".log")]

if len(log_files) != 1:
    print("!! Please make sure there is only ONE .log file in the 'logs' folder.")
    exit()

log_file_name = log_files[0]
log_file_path = os.path.join(logs_folder, log_file_name)

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

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"compliance_report_{timestamp}.txt"
    report_path = os.path.join("reports", report_filename)

    with open(report_path, "w") as report_file:
        report_file.write("=== Compliance Summary === \n\n")

        if failed_login_counts:
            report_file.write("Failed Login Attempts:\n")
            for user, count in failed_login_counts.items():
                report_file.write(f" - {user}: {count} failed attempt(s)\n")

            alert_triggered = False
            report_file.write("\nPotential Security Alerts:\n")
            for user, count in failed_login_counts.items():
                if count >= 3:
                    alert_triggered = True
                    report_file.write(f" !! ALERT: {user} had {count} failed logins\n")
                    print(f"ALERT: {user} had {count} filed login attempts!")

            if not alert_triggered:
                report_file.write(" No users exceeded login failure threshold.\n")
        else:
            report_file.write("No failed logins found.\n")

        if expired_certs:
            report_file.write("\nExpired Certificates:\n")
            for cert in expired_certs:
                report_file.write(f" - {cert}\n")
        else:
            report_file.write("\nNo expired certifications found. \n")

    print(f"\nSummary saved to: {report_path}")

    archived_log_path = os.path.join(archive_folder, log_file_name)
    shutil.move(log_file_path, archived_log_path)
    print(f"Archived log file to: {archived_log_path}")

    now = time.time()
    delete_threshold_seconds = 10 * 60

    deleted_files = 0
    for filename in os.listdir(archive_folder):
        file_path = os.path.join(archive_folder, filename)
        if os.path.isfile(file_path):
            file_age = now - os.path.getmtime(file_path)
            if file_age > delete_threshold_seconds:
                os.remove(file_path)
                deleted_files += 1
    if deleted_files > 0:
        print(f"Cleaned up {deleted_files} old archived log(s).")

else:
    print("Log file not found.")
