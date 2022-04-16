from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    photo = models.ImageField(upload_to="profile/photos", null=True, blank=True)

@receiver(pre_save, sender=get_user_model())
def generate_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
