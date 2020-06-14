from django.forms import ModelForm, Form
from django.contrib.auth.forms import UserCreationForm
from .models import User, Product
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
				  'email' : 'Mail :',
				  }
		widgets = {
			'email' : forms.EmailInput()
		}

class PickProduct(ModelForm):
	class Meta:
		model = Product
		fields = ['qrcode']
		labels = {
			'qrcode' : 'Qr Code :'
		}