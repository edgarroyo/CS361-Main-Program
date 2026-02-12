import json
import os

DATA_FILE = "data.json"

def load_destinations():
    # If file doesn't exist, start with an empty list
    if not os.path.exists(DATA_FILE):
        return []

    # If file exists but is empty, treat as empty list
    if os.path.getsize(DATA_FILE) == 0:
        return []

    # If file exists but contains invalid JSON, fail gracefully
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            # Ensure it’s the type we expect
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []

def save_destinations(destinations):
    with open(DATA_FILE, "w") as file:
        json.dump(destinations, file, indent=2)
