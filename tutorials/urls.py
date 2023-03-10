from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.about , name='about'),
    path('', views.login , name='login'),
    path('', views.register, name='register'),
    path('', views.tutorial_1, name='tutorial_1'),
    path('', views.tutorial_2 , name='tutorial_2'),
    path('', views.tutorial_3 , name='tutorial_3'),
]
