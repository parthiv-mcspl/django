
# users/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileEditForm, CollaborationRequestForm
from .models import UserProfile, CollaborationRequest
from django.contrib.auth.models import User
# In your views.py

@login_required
def edit_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile = get_object_or_404(UserProfile, user=user)
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = UserProfileEditForm(instance=profile)
    return render(request, 'users/edit_profile.html', {'form': form})

@login_required
def send_collaboration_request(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)
    if request.method == 'POST':
        form = CollaborationRequestForm(request.POST)
        if form.is_valid():
            collab_request = form.save(commit=False)
            collab_request.sender = request.user
            collab_request.receiver = receiver
            collab_request.save()
            return redirect('profile_list')
    else:
        form = CollaborationRequestForm()
    return render(request, 'users/send_collaboration_request.html', {'form': form, 'receiver': receiver})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileEditForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
            login(request, user)
            return redirect('profile_list')
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileEditForm()
    return render(request, 'users/register.html', {'user_form': user_form, 'profile_form': profile_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile_list')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid login'})
    return render(request, 'users/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

# users/views.py

@login_required
def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'users/profile_list.html', {'profiles': profiles})

@login_required
def profile_detail(request, user_id):
    profile = get_object_or_404(UserProfile, user__id=user_id)
    return render(request, 'users/profile_detail.html', {'profile': profile})
