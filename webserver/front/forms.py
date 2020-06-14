from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class LoginForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
		labels = {'username' : 'Username :',
				  'password' : 'Password :'}
		widgets = {
			'password' : forms.PasswordInput()
		}

class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email']
		labels = {'username' : 'Username :',
				  'email' : 'Mail',
				  }
		widgets = {
			'email' : forms.EmailInput()
		}