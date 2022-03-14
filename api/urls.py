from django.urls import include, path

urlpatterns = [
    path("account/", include("account.urls")),
    path("posts/", include("blog.urls")),
]
