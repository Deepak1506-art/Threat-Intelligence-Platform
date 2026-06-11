from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    with open("../data/normalized_threats.json", "r") as f:
        threats = json.load(f)

    total_threats = len(threats)
    high_risk = len([t for t in threats if t["risk_score"] >= 80])

    return render_template(
        "index.html",
        total_threats=total_threats,
        high_risk=high_risk,
        threats=threats
    )

if __name__ == "__main__":
    app.run(debug=True)