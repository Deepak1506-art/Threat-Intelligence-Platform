from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Threat(db.Model):
    __tablename__ = "threats"

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(50), nullable=False)
    domain = db.Column(db.String(100))
    threat_type = db.Column(db.String(50))
    severity = db.Column(db.String(20))
    risk_score = db.Column(db.Integer)
    source = db.Column(db.String(100))
    country = db.Column(db.String(50))
    status = db.Column(db.String(20))

    def __repr__(self):
        return f"<Threat {self.ip}>"