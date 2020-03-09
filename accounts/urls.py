from django.urls import path, include
from .views import loginView, logoutView, registerView, profileView, registerDonorView

urlpatterns = [
	path('login/', loginView, name="login"),
	path('logout/', logoutView, name="logout"),
	path('register/', registerView, name="register"),
	path('profile/', profileView, name="profile"),
	path('register-donor/',registerDonorView, name="register-donor"),
]