# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('collaborate/<int:receiver_id>/', views.send_collaboration_request, name='send_collaboration_request'),
    
    path('edit-profile/<int:user_id>/', views.edit_profile, name='edit_profile'),

    path('', views.user_login, name='home'),  # Set home page to login
]
