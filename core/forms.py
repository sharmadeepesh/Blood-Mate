from django.forms import ModelForm
from .models import group, Donor

class registerDonorForm(ModelForm):
	class Meta:
		model = Donor
		fields = ['blood_group','age','phone_number','occupation','country','state','zipcode']
		#fields = '__all__'