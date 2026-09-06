import json
import os
from datetime import datetime, timezone


DB_FILE = "users.json"
LOG_FILE = "audit_log.json"
login_attempts = {}


def load_users():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_users(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

def log_audit(email, status, ip):
    entry = {
        "email": email,
        "status": status,
        "ip": ip,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    logs.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

def check_rate_limit(ip):
    now = datetime.now(timezone.utc).timestamp()
    attempts = login_attempts.get(ip, [])
    attempts = [t for t in attempts if now - t < 60]
    login_attempts[ip] = attempts
    return len(attempts) < 5

def record_attempt(ip):
    now = datetime.now(timezone.utc).timestamp()
    if ip not in login_attempts:
        login_attempts[ip] = []
    login_attempts[ip].append(now)
