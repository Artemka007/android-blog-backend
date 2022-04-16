from django.conf import settings
from django.http import HttpRequest
from django.utils.deprecation import MiddlewareMixin


class DisableCSRF(MiddlewareMixin):
   def process_request(self, request: HttpRequest):
      setattr(request, '_dont_enforce_csrf_checks', True)
