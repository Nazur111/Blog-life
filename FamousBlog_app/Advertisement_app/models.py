from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User




class AdvertisementList(models.Model):
    name = models.CharField("Назва списку", max_length=255)
    description = models.TextField("Опис", blank=True)
    deadline = models.DateField("Дедлайн", null=True, blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ad_lists'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("list_detail", args=[self.id])


class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    content = models.TextField("Опис")
    created_at = models.DateTimeField("Створено", auto_now_add=True)
    deadline = models.DateField("Дедлайн", null=True, blank=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='advertisements'
    )

    list = models.ForeignKey(
        AdvertisementList,
        on_delete=models.CASCADE,
        related_name="advertisements",
        null=True,
        blank=True,
        verbose_name="Список"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("advertisement_detail", args=[self.id])
