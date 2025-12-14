from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Blog(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='blogs')