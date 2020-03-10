import django_filters
from .models import *

class donorFilter(django_filters.FilterSet):
	class Meta:
		model = Donor 
		fields = ['blood_group','age','country','state','zipcode','urgent_available']