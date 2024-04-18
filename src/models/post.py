from dataclasses import dataclass
import uuid

@dataclass 
class Post:
    id: uuid.UUID
    user_id: uuid.UUID
    content: str
    banner: str
    approved: bool

    def __post_init__(self):
        if type(self.id) is not uuid.UUID:
            self.id = uuid.UUID(self.id)