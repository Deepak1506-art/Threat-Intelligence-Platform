import json
import os

THREATS_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "threats.json")
NORMALIZED_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "normalized_threats.json")

def normalize_threats():

    with open(THREATS_PATH, "r") as f:
        threats = json.load(f)

    unique_ips = set()
    normalized = []

    for threat in threats:
        if threat["ip"] not in unique_ips:
            unique_ips.add(threat["ip"])
            normalized.append(threat)

    with open(NORMALIZED_PATH, "w") as f:
        json.dump(normalized, f, indent=4)

    return normalized