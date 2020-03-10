from django.shortcuts import render, redirect
from core.forms import registerDonorForm

from django.contrib.auth.models import User
from .models import Donor
from .filters import donorFilter

# Create your views here.

def donorProfileView(request, username):
	user = User.objects.filter(username=username)
	if user.exists():
		donor = Donor.objects.filter(user=user[0])
		if donor.exists():
			context = {
				'donor':donor[0],
			}
			return render(request, "core/donorprofile.html", context = context)
		else:
			return redirect('register-donor')
	else:
		return redirect('register')

def registerDonorView(request):
	form = registerDonorForm()
	if request.method == "POST":
		form = registerDonorForm(request.POST)
		
		if form.is_valid():
			temp = form.save(commit=False)
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

def landingPageView(request):
	return render(request,"core/landingpage.html")

def searchView(request):
	donors = Donor.objects.all()
	donorfilter = donorFilter(request.GET, queryset=donors)
	donors = donorfilter.qs
	if donors.exists():
		context = {
			'donors':donors,
			'filter':donorfilter,
		}
		return render(request, 'core/search.html', context=context)
	else:
		return render(request, 'core/no_donors.html')
	