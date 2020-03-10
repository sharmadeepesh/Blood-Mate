from django.urls import path, include
from .views import loginView, logoutView, registerView, profileView, donorSettingsView

urlpatterns = [
	path('login/', loginView, name="login"),
	path('logout/', logoutView, name="logout"),
	path('register/', registerView, name="register"),
	path('profile/', profileView, name="profile"),
	path('settings/',donorSettingsView, name="settings"),
	path('logout/', logoutView, name="logout"),
]