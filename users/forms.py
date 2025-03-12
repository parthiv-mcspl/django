# users/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, CollaborationRequest

class CollaborationRequestForm(forms.ModelForm):
    class Meta:
        model = CollaborationRequest
        fields = ('name', 'hobby', 'email', 'contact_no', 'message')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('photo', 'hobby', 'contact_no','detail')
