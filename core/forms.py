from django.forms import ModelForm
from .models import group, Donor

class registerDonorForm(ModelForm):
	class Meta:
		model = Donor
		fields = ['first_name','last_name','blood_group','age','phone_number','occupation','country','state','zipcode','urgent_available']
		#fields = '__all__'