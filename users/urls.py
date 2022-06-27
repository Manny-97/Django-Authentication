from django.urls import URLPattern, path
from . import apis
from users.apis import RegisterApi

urlpatterns = [
    path("register/", apis.RegisterApi.as_view(), name="register"),
    path("login/", apis.LoginApi.as_view(), name="login"),
    path("me/", apis.UserApi.as_view(), name="me"),
]