from click import password_option
from django.shortcuts import render
from rest_framework import views, exceptions, permissions, response

from . import serializer as user_serializer
from . import service, authentication
class RegisterApi(views.APIView):
    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        serializer.instance = service.create_user(user_dc=data)
        print(data)
        return response.Response(data=serializer.data)

class LoginApi(views.APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        user = service.user_email_selector(emai=email)
# We don't want to tell the user which of the login details is actually wrong
        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")

        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")

        token = service.create_token(user_id=user.id)
        resp = response.Response()
        resp.set_cookie(key="jwt", value=token, httponly=True)

        return resp

class UserApi(views.APIView):
    """
        Only works for authenticated users
    """
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = user_serializer.UserSerializer(user)
        return response.Response(serializer.data)

class LogoutApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "Thank you, You have now succesfully logout"}
        return resp