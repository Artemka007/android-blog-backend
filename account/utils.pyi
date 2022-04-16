from rest_framework.views import Request

from .models import User


def auth(request: Request) -> User | None: ...
def get_token(username: str, password: str) -> str | None: ...
