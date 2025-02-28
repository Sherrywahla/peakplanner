from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "bio", "profile_picture"]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["bio", "profile_picture"]
