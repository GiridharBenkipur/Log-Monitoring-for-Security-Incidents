# main.py
from log_parser import parse_log, detect_brute_force
from alert import send_email_alert

if __name__ == "__main__":
    # Parse log file for failed login attempts
    failed_attempts = parse_log()

    # Detect brute force attacks
    attackers = detect_brute_force(failed_attempts, threshold=5)

    # Ask user for email addresses
    email_list = input("Enter email addresses separated by commas: ").split(",")

    # Send alert if brute-force detected
    send_email_alert(attackers, email_list)