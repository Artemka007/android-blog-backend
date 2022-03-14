from django.utils.deprecation import MiddlewareMixin

from account.utils import auth


class AuthMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        if not request.user.is_authenticated:
            user = auth(request)
            if user:
                request.user = user
        return None
