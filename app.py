from flask import Flask, render_template, request
from config import Config
from models.models import db
from services.collector import collect_threats
from services.normalizer import normalize_threats
from services.policy import enforce_policy

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():

    threats = collect_threats()

    normalize_threats()

    blocked = enforce_policy()

    search = request.args.get("search", "").strip().lower()

    if search:
        threats = [
            t for t in threats
            if search in t["ip"].lower()
            or search in t["domain"].lower()
        ]

    total = len(threats)

    high_risk = len([
        t for t in threats
        if t["risk_score"] >= 80
    ])

    severity_data = {
        "Critical": len([
            t for t in threats
            if t["risk_score"] >= 90
        ]),
        "High": len([
            t for t in threats
            if 70 <= t["risk_score"] < 90
        ]),
        "Medium": len([
            t for t in threats
            if 40 <= t["risk_score"] < 70
        ]),
        "Low": len([
            t for t in threats
            if t["risk_score"] < 40
        ])
    }

    return render_template(
        "index.html",
        threats=threats,
        total=total,
        high_risk=high_risk,
        blocked=len(blocked),
        severity_data=severity_data,
        search=search
    )


if __name__ == "__main__":
    app.run(debug=True)