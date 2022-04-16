from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from utils.security import decrypt_string


def auth(request):
    key = request.META.get("HTTP_AUTHORIZATION")

    if key is None:
        return None

    key = decrypt_string(key)

    try:
        token = Token.objects.get(pk=key)
    except:
        return None
    
    return token.user

def get_token(username, password):
    user = authenticate(username=username, password=password)
    if user is None:
        return None
    else:
        return user.auth_token
