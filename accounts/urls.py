from django.urls import path, include
from .views import loginView, logoutView, registerView, dashboardView, profileSettingsView

urlpatterns = [
	path('login/', loginView, name="login"),
	path('logout/', logoutView, name="logout"),
	path('register/', registerView, name="register"),
	path('dashboard/', dashboardView, name="dashboard"),
	path('settings/',profileSettingsView, name="settings"),
	path('logout/', logoutView, name="logout"),
]