from django.db import models
from users.models import User

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs')
    activity = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity} at {self.timestamp}"