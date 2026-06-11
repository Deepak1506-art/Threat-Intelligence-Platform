import json

with open("../data/threats.json", "r") as f:
    threats = json.load(f)

unique_ips = set()
normalized = []

for threat in threats:
    if threat["ip"] not in unique_ips:
        unique_ips.add(threat["ip"])
        normalized.append(threat)

with open("../data/normalized_threats.json", "w") as f:
    json.dump(normalized, f, indent=4)

print("Threats normalized successfully.")