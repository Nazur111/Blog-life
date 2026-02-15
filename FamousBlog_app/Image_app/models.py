from django.db import models

class ImageFile(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title or f"Image {self.id}"
