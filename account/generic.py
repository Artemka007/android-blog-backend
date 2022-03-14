from django.utils.translation import gettext_lazy as _
from rest_framework.views import Response

from utils import status_codes


class AuthorizationMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            response = Response({
                "code": status_codes.UNAUTHORIZED,
                "message": _("User did not authorized."),
                "data": {}
            })
            response.rendered_content = {}
            return response
