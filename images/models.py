from django.db import models
from users.models import User

class Image(models.Model):
    file = models.ImageField(upload_to='images/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} by {self.uploaded_by.username}"