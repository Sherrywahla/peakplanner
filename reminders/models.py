from django.db import models
from django.conf import settings

class Reminder(models.Model):
    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("In progress", "In Progress"),
        ("completed", "Completed"),
    ]
    title = models.CharField(max_length=255, default="")
    message = models.CharField(max_length=255)
    remind_at = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="Medium")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"Reminder: {self.message} at {self.remind_at}"

