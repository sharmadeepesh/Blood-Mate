from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

class registerForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','username','email','password1','password2']

