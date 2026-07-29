import json
import os
import random

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "threats.json"
)


def collect_threats():

    domains = [
        "malicious-example.com",
        "phishing-example.net",
        "botnet-example.org",
        "trojan-site.com",
        "ransomware.net",
        "spyware.org",
        "wormattack.com",
        "dangerhost.net",
        "evilserver.org",
        "hackzone.com"
    ]

    threats = []

    for i in range(1, 51):

        threat = {
            "ip": f"192.168.{random.randint(1,20)}.{random.randint(1,254)}",
            "domain": random.choice(domains),
            "risk_score": random.randint(20, 100)
        }

        threats.append(threat)

    with open(DATA_PATH, "w") as f:
        json.dump(threats, f, indent=4)

    return threats