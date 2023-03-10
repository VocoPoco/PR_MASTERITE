from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
  template = loader.get_template('templates/mainLoginPage.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('templates/aboutPage.html')
  return HttpResponse(template.render())

def login(request):
  template = loader.get_template('templates/loginPage.html')
  return HttpResponse(template.render())

def register(request):
  template = loader.get_template('templates/registerPage.html')
  return HttpResponse(template.render())

def tutorial_1(request):
  template = loader.get_template('templates/tutorial1.html')
  return HttpResponse(template.render())

def tutorial_2(request):
  template = loader.get_template('templates/tutorial2.html')
  return HttpResponse(template.render())

def tutorial_3(request):
  template = loader.get_template('templates/tutorial3.html')
  return HttpResponse(template.render())