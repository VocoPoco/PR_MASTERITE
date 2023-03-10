from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate



def home(request):
  template = loader.get_template('mainLoginPage.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('aboutPage.html')
  return HttpResponse(template.render())

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("dashboard")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="loginPage.html", context={"login_form":form})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.") # move it to the registration not the admin part
	form = NewUserForm()
	return render (request=request, template_name="registerPage.html", context={"register_form":form})
#   template = loader.get_template('registerPage.html')
#   return HttpResponse(template.render())

def dashboard_request(request):
  template = loader.get_template('homePage.html')
  return HttpResponse(template.render())

def tutorial_1(request):
  template = loader.get_template('tutorial1.html')
  return HttpResponse(template.render())

def tutorial_2(request):
  template = loader.get_template('tutorial2.html')
  return HttpResponse(template.render())

def tutorial_3(request):
  template = loader.get_template('tutorial3.html')
  return HttpResponse(template.render())