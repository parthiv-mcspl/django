# users/admin.py

from django.contrib import admin
from .models import UserProfile, CollaborationRequest

admin.site.register(UserProfile)
admin.site.register(CollaborationRequest)
