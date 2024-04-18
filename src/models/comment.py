from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
import uuid

from extensions import db


@dataclass
class Comment(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: uuid.UUID = db.Column(db.String(36), nullable=False)
    post_id: uuid.UUID = db.Column(db.String(36), nullable=False)
    parent_id: uuid.UUID = db.Column(db.String(36), nullable=True)
    content: str = db.Column(db.String, nullable=False)

    def __post_init__(self):
        self.user_id = self._convert_to_uuid(self.user_id)
        self.post_id = self._convert_to_uuid(self.post_id)
        self.parent_id = self._convert_to_uuid(self.parent_id) if self.parent_id else None

    @staticmethod
    def _convert_to_uuid(value):
        if not isinstance(value, uuid.UUID):
            return uuid.UUID(value)
        return value
