from dataclasses import dataclass
import uuid
from flask_sqlalchemy import SQLAlchemy
from extensions import db

@dataclass
class User(db.Model):
    id: uuid.UUID = db.Column(db.String(36), primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    email: str = db.Column(db.String(100), nullable=False, unique=True)
    password: str = db.Column(db.String, nullable=False)
    is_admin: bool = db.Column(db.Boolean, default=False, nullable=False)

    def __post_init__(self):
        self.id = self._convert_to_uuid(self.id)

    @staticmethod
    def _convert_to_uuid(value):
        if not isinstance(value, uuid.UUID):
            return uuid.UUID(value)
        return value
