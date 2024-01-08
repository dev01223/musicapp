from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *

class ClienteRegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2',  'username']



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email ou CPF'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Senha'}))