from django.urls import path, include
from .views import loginView, logoutView, registerView, profileView

urlpatterns = [
	path('login/', loginView, name="login"),
	path('logout/', logoutView, name="logout"),
	path('register/', registerView, name="register"),
	path('profile/', profileView, name="profile"),
]