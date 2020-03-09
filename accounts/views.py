from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

from .forms import registerForm, registerDonorForm

# Create your views here.

def registerDonorView(request):
	user = request.user
	form = registerDonorForm(initial = {'user':user})
	if request.method == "POST":
		form = registerDonorForm(request.POST)
		
		if form.is_valid():
			temp = form.save(commit=false)
			temp.user = request.user
			temp.save()
			return redirect('profile')
		else:
			return redirect('register-donor')

	else:
		context = {
		'form':form,
		}
		return render(request,'core/registerdonor.html', context = context)

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
	logout(request, user)
	return redirect('login')

def profileView(request):
	return HttpResponse("User Profile")