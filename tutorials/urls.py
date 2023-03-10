from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ping/', views.login.ping, name='ping'),
    path('login/', views.login.login, name='login'),
    path('register/', views.login.register , name='register'),
    path('tutorial_edit/', views.tutorial.tutorial_edit, name='tutorial_edit'),
    path('tutorial_create/', views.tutorial.tutorial_create, name='tutorial_create'),
    path('user_edit/', views.user.user_edit , name='user_edit'),
]
