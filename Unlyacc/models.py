# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('message-detail',kwargs={'pk':self.pk})
