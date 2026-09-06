import json
import os

FILES = {
    "employees": "employees.json",
    "shift_types": "shift_types.json",
    "assignments": "assignments.json",
    "swaps": "swaps.json",
    "attendance": "attendance.json",
}


def load_all(category):
    path = FILES.get(category, "")
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)


def save_all(category, data):
    path = FILES.get(category, "")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def gen_id(data):
    if not data:
        return 1
    return max(int(k) for k in data.keys()) + 1
