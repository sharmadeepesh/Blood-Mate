from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class country(models.Model):
	name = models.CharField(max_length = 20)

	def __str__(self):
		return str(self.name)

class zipCode(models.Model):
	code = models.CharField(max_length=10)

	def __str__(self):
		return str(self.code)

class state(models.Model):
	name = models.CharField(max_length=20)
	country = models.ForeignKey(country, on_delete = models.CASCADE)
	zipcode = models.ForeignKey(zipCode, on_delete = models.PROTECT)

	def __str__(self):
		return str(self.name)


class group(models.Model):
	name = models.CharField(max_length=3)
	receives = models.CharField(max_length = 30)

	def __str__(self):
		return str(self.name)

class Donor(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	blood_group = models.OneToOneField(group, on_delete = models.SET_NULL, null=True)
	age = models.IntegerField()
	phone_number = models.IntegerField()
	occupation = models.CharField(max_length = 50)
	country = models.OneToOneField(country, on_delete=models.SET_NULL, null=True)
	state = models.OneToOneField(state, on_delete = models.SET_NULL, null=True)
	zipcode = models.OneToOneField(zipCode, on_delete = models.SET_NULL, null=True)
	urgent_available = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username + ' >> ' + self.user.email