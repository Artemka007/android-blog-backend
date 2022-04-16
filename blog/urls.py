from django.urls import path

from blog.views import PostCommentsView, PostLikeView, PostView

urlpatterns = [
    path("", PostView.as_view()),
    path("like/", PostLikeView.as_view()),
    path("comments/", PostCommentsView.as_view()),
]
