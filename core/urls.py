from django.urls import path, include

from .views import registerDonorView, landingPageView

urlpatterns = [
	path('register-donor/', registerDonorView, name="register-donor"),
	path('', landingPageView, name="homepage"),
]