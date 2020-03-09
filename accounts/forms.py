from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from core.models import group, Donor

class registerForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','username','email','password1','password2']

class registerDonorForm(ModelForm):
	class Meta:
		model = Donor
		#fields = ['blood_group','age','phone_number','occupation','country','state','zipcode']
		fields = '__all__'