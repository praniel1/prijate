from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    userim = models.ForeignKey(User, null=True)
    avatar = models.TextField(null=True)