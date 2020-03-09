from django.shortcuts import render
from core.forms import registerDonorForm

# Create your views here.
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