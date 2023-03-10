from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.about , name='about'),
    path('', views.login , name='login'),
    path('', views.register, name='register'),
    path('', views.tutorial1, name='tutorial1'),
    path('', views.tutorial2 , name='tutorial2'),
    path('', views.tutorial3 , name='tutorial3'),
]
