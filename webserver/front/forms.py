from django.forms import ModelForm
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