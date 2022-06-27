from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import models as auth_models
from django.forms import CharField
# Create your models here.

# for creating a user via the django cli
class UserManager(auth_models.BaseUserManager):
    def create_user(self, name: str, phone_number: int, email: str, password: str=None, is_superuser=False, is_staff=False) -> "User":
        if not email:  #Validation
            raise ValueError("User must have an email")
        if not name:
            raise ValueError("User must have a name")
        if not phone_number:
            raise ValueError("User must have a valid Nigeria phone number")

        user = self.model(email=self.normalize_email(email))
        user.name = name
        user.phone_number = phone_number
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user
    
    def create_superuser(self, name: str, email: str, password:str, phone_number: int) -> "User":
        user = self.create_user(
            name= name,
            email=email,
            password=password,
            phone_number=phone_number,
            is_staff=True,
            is_superuser=True
        )
        user.save()

class User(auth_models.AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    username = None
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number']