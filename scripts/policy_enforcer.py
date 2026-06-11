import json

with open("../data/normalized_threats.json", "r") as f:
    threats = json.load(f)

with open("../blocked_ips.txt", "w") as file:
    for threat in threats:
        if threat["risk_score"] >= 80:
            file.write(threat["ip"] + "\n")
            print(f"Blocked: {threat['ip']}")

print("Policy enforcement completed.")