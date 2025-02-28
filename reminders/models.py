from django.db import models
from django.conf import settings

class Reminder(models.Model):
    message = models.CharField(max_length=255)
    remind_at = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reminder: {self.message} at {self.remind_at}"

