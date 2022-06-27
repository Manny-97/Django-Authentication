import dataclasses
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import User
@dataclasses.dataclass
class UserDataclass:
    name: str
    phone_number: str
    email: str
    password: str = None
    id: int = None

    @classmethod
    def from_instance(cls, users:"User") -> "UserDataclass":
        return cls(
            name=user.name,
            phone_number=user.phone_number,
            email=user.email,
            id=user.id
        )