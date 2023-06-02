from django.db import models
from django.contrib.auth.models import User


class UserAvatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    avatar = models.CharField(null=True, max_length=300)
