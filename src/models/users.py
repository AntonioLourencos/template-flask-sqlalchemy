import json
from config.database import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), unique=True, nullable=False)

    def to_json(self):
        response = {}

        for attr, value in self.__dict__.items():
            if not attr.startswith("_"):
                response.__setitem__(attr, value)

        return response

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
