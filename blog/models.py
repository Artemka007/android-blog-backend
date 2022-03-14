from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(
        to=get_user_model(), 
        on_delete=models.CASCADE, 
        related_name="posts"
    )

    body = models.TextField()

    created_time = models.DateTimeField(auto_created=True)
    updated_time = models.DateTimeField(auto_now=True)

    likes = models.ManyToManyField(
        to=get_user_model(), 
        related_name="post_likes"
    )

    def __str__(self):
        return self.body[:100]

class PostComment(models.Model):
    user = models.ForeignKey(
        to=get_user_model(), 
        on_delete=models.CASCADE, 
        related_name="comments"
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    body = models.TextField()

    created_time = models.DateTimeField(auto_created=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:100]
