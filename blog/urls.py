from django.urls import path

from blog.views import PostLikeView, PostView

urlpatterns = [
    path("", PostView.as_view()),
    path("like/", PostLikeView.as_view())
]
