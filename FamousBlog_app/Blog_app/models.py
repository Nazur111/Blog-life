from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField("Назва блогу", max_length=100)
    description = models.TextField("Опис блогу")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blogs",
        verbose_name="Автор"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")
