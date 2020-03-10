from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

from .forms import registerForm

# Create your views here.

def registerView(request):
	form = registerForm()

	if request.method == "POST":
		form = registerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
		else:
			return redirect('register')

	else:
		context = {
		'form':form,
		}
		return render(request,'accounts/register.html', context = context)

def loginView(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('profile')
		else:
			return redirect('login')
	else:
		return render(request, "accounts/login.html")

def logoutView(request):
	logout(request)
	return redirect('login')

def profileView(request):
	user = request.user
	context = {
		'username':user.username,
	}
	return render(request,'accounts/profile.html',context = context)

def profileSettingsView(request):
	user = request.user
	context = {
		'username':user.username,
	}
	return render(request,'accounts/settings.html', context = context)