from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    hobby = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15)
    detail = models.CharField(max_length=255, default='your_default_value')
    def __str__(self):
        return self.user.username

class CollaborationRequest(models.Model):
    sender = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    email = models.EmailField(default='default@example.com')
    contact_no = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username}"
