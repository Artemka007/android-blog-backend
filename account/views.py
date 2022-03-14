from django.shortcuts import render
from rest_framework.views import APIView, Response

from account.generic import AuthorizationMixin
from account.serializers import UserSerializer
from account.utils import get_token
from utils import status_codes


class AccountView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({
                "code": status_codes.UNAUTHORIZED,
                "message": "User did not authorized."
            })
        serializer = UserSerializer(request.user)
        return Response({
            "code": status_codes.INFO,
            "message": "Profile has been returned",
            "data": serializer.data
        })

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        token = get_token(username, password)

        if token is None:
            data = {
                "code": status_codes.ERROR,
                "message": "You did not registered."
            }
        else:
            data = {
                "code": status_codes.SUCCESS,
                "message": "You was successfuly logined.",
                "data": {
                    "token": token.key
                }
            }

        return Response(data)
