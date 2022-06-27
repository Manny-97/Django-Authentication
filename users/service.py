import dataclasses
from typing import TYPE_CHECKING

from click import password_option
from . import models
from pytest import Instance

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
            name=users.name,
            phone_number=users.phone_number,
            email=users.email,
            id=users.id
        )
# Create user
def create_user(user_dc: "UserDataclass") -> "UserDataclass":
    instance = models.User(
        name=user_dc.name,
        phone_number=user_dc.phone_number,
        email=user_dc.email
    )
    if user_dc.password is not None:
        instance.set_password(user_dc.password)

    instance.save()
    return UserDataclass.from_instance(instance)

def user_email_selector(email: str) -> "User":
    user = models.User.objects.filter(email=email).first()

    return user