# log_parser.py
import re
import logging
from config import LOG_FILE_PATH

# Configure logging
logging.basicConfig(filename="log_monitor.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Regex pattern to match failed SSH login attempts
FAILED_LOGIN_PATTERN = r"Failed password for .* from (\d+\.\d+\.\d+\.\d+) port (\d+)"

def parse_log():
    """Parse log file and return failed login attempts by IP."""
    failed_attempts = {}

    try:
        with open(LOG_FILE_PATH, "r") as file:
            for line in file:
                match = re.search(FAILED_LOGIN_PATTERN, line)
                if match:
                    ip = match.group(1)
                    failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
    except FileNotFoundError:
        logging.error("Log file not found! Check the LOG_FILE_PATH in config.py")
    
    return failed_attempts

def detect_brute_force(failed_attempts, threshold=5):
    """Detect brute force attempts exceeding threshold."""
    attackers = {ip: count for ip, count in failed_attempts.items() if count >= threshold}
    return attackers
