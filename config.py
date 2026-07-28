import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "threat-intelligence-platform"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database", "threat_platform.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False