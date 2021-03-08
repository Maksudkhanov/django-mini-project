from urllib import request

from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)
    published = models.BooleanField(default=True)


    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

