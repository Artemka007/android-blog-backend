from django.urls import path

from account.views import AccountView, LoginView

urlpatterns = [
    path("", AccountView.as_view(), name="api_account"),
    path("login/", LoginView.as_view(), name="api_login")
]
