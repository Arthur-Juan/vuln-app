from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
import uuid

from extensions import db


@dataclass
class Post(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: uuid.UUID = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    title: str = db.Column(db.Text, nullable=False)
    content: str = db.Column(db.Text, nullable=False)
    banner: str = db.Column(db.String, nullable=True)
    approved: bool = db.Column(db.Boolean, nullable=False)

    def __post_init__(self):
        self.id = self._convert_to_uuid(self.id)
        self.user_id = self._convert_to_uuid(self.user_id)

    @staticmethod
    def _convert_to_uuid(value):
        if not isinstance(value, uuid.UUID):
            return uuid.UUID(value)
        return value
