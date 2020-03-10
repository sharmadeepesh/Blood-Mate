from django.urls import path, include

from .views import registerDonorView, landingPageView, searchView, donorProfileView

urlpatterns = [
	path('register-donor/', registerDonorView, name="register-donor"),
	path('', landingPageView, name="homepage"),
	path('search/', searchView, name="search"),
	path('donor-profile/<str:username>', donorProfileView, name="donor-profile"),
]
