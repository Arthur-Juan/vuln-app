from dataclasses import dataclass
import uuid

from flask_sqlalchemy import SQLAlchemy

@dataclass
class Comment:
    user_id: uuid
    post_id: uuid
    parent_id: uuid
    content: str

    def __post_init__(self):
        if type(self.id) is not uuid.UUID:
            self.id = uuid.UUID(self.id)