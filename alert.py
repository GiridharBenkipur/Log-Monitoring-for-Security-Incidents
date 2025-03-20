# alert.py
import smtplib
from email.mime.text import MIMEText
from config import SMTP_SERVER, SMTP_PORT, EMAIL_SENDER, EMAIL_PASSWORD

def send_email_alert(attackers, email_list):
    """Send an email alert when brute-force attack is detected."""
    if not attackers:
        return  # No brute-force attacks detected

    # Create email content
    subject = "Security Alert: SSH Brute Force Detected"
    message = "The following IPs attempted multiple failed SSH logins:\n\n"
    for ip, attempts in attackers.items():
        message += f"IP: {ip} | Failed Attempts: {attempts}\n"

    # Email setup
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = ", ".join(email_list)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure connection
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, email_list, msg.as_string())
        print("Alert Sent Successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
