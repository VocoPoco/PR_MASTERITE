from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.about , name='about'),
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('dashboard/', views.dashboard_request, name='dashboard')
    # path('', views.tutorial_1, name='tutorial_1'),
    # path('', views.tutorial_2 , name='tutorial_2'),
    # path('', views.tutorial_3 , name='tutorial_3'),
]
