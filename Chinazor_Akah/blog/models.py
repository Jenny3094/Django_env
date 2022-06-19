from msilib.schema import PublishComponent
from multiprocessing import AuthenticationError
# from readline import get_current_history_length
from turtle import title
from typing import Text
from django.conf import settings
from django.db import models

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField(max_length= 100)
    Author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()