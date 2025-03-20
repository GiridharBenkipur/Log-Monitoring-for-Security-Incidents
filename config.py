import os

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

if not EMAIL_SENDER or not EMAIL_PASSWORD:
    raise ValueError("Missing environment variables! Set EMAIL_SENDER and EMAIL_PASSWORD.")

# config.py

# Log file path (change based on your OS)
LOG_FILE_PATH = "sample_logs/auth.log"

# Brute force detection threshold
FAILED_ATTEMPT_THRESHOLD = 5

# Email settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"