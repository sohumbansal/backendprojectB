# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from myapp.models import CustomUser  # Add this import line

class SignUpForm(UserCreationForm):
    # Customize your signup form if needed
    class Meta:
        model = CustomUser  # Use the correct reference to the CustomUser model
        fields = ('username', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    # Customize your login form if needed
    class Meta:
        model = CustomUser  # Use the correct reference to the CustomUser model
        fields = ('username', 'password')
