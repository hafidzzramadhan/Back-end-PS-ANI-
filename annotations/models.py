from django.db import models
from users.models import User
from images.models import Image

class Annotation(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='annotations')
    label = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='annotations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.label} on Image {self.image.id}"