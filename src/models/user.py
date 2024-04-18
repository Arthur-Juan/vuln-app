from dataclasses import dataclass
import uuid

@dataclass
class User:
    id: uuid.UUID
    name: str
    email: str
    password: str
    is_admin: bool 

    def __post_init__(self):
        if type(self.id) is not uuid.UUID:
            self.id = uuid.UUID(self.id)