from django.contrib import admin
from .models import group, Donor, country, state, zipCode
# Register your models here.

admin.site.register(group)
admin.site.register(Donor)
admin.site.register(country)
admin.site.register(state)
admin.site.register(zipCode)