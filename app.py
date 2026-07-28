from flask import Flask, render_template
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

    total = len(threats)

    high_risk = len([t for t in threats if t["risk_score"] >= 80])

    return render_template(
        "index.html",
        threats=threats,
        total=total,
        high_risk=high_risk,
        blocked=len(blocked)
    )


if __name__ == "__main__":
    app.run(debug=True)