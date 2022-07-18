from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'website_url', 'bio']
        # exclude = ['first_name', 'last_name']
