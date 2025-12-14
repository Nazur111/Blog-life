from django.db import models
from django.contrib.auth.models import User
from Categorys_app.models import Category
from Image_app.models import ImageFile

STATUS_CHOICES = (
    ("draft", "Чернетка"),
    ("published", "Опублікована"),
)

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    images = models.ManyToManyField(ImageFile, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

