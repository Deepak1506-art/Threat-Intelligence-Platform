import json
import os

NORMALIZED_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "normalized_threats.json")
BLOCKED_PATH = os.path.join(os.path.dirname(__file__), "..", "blocked_ips.txt")

def enforce_policy():

    with open(NORMALIZED_PATH, "r") as f:
        threats = json.load(f)

    blocked = []

    with open(BLOCKED_PATH, "w") as file:
        for threat in threats:
            if threat["risk_score"] >= 80:
                file.write(threat["ip"] + "\n")
                blocked.append(threat["ip"])

    return blocked