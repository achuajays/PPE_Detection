import os
import json
from datetime import datetime
import config

def initialize_log_file():
    """Initialize log file if it doesn't exist"""
    if not os.path.exists(config.LOG_FILE):
        with open(config.LOG_FILE, 'w') as f:
            json.dump([], f)

def log_violation(missing_ppe_list):
    """Log violation to JSON file"""
    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    violation_text = ", ".join([f"No {item}" for item in missing_ppe_list])

    log_entry = {
        "timestamp": timestamp,
        "violation": violation_text
    }

    # Read existing logs
    try:
        with open(config.LOG_FILE, 'r') as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    # Add new log entry
    logs.append(log_entry)

    # Write back to file
    with open(config.LOG_FILE, 'w') as f:
        json.dump(logs, f, indent=2)

    print(f"📝 Logged violation: {violation_text} at {timestamp}")

def print_status_update(all_ppe_present):
    """Print periodic status update"""
    current_time = datetime.now().strftime('%H:%M:%S')
    if all_ppe_present:
        print(f"✅ Status Update: All PPE compliant at {current_time}")
    else:
        print(f"🚨 Status Update: Safety violation ongoing at {current_time}")