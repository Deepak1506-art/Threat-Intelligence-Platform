from services.collector import collect_threats
from services.normalizer import normalize_threats
from services.policy import enforce_policy

print("Collecting threats...")
collect_threats()

print("Normalizing threats...")
normalize_threats()

print("Applying policy...")
blocked = enforce_policy()

print("Blocked IPs:")
print(blocked)