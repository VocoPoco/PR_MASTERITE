from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.about , name='about'),
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('dashboard/', views.dashboard_request, name='dashboard'),
    path('dashboard/', include([
        path('tutorial-1/', views.tutorial_1_request, name='tutorial_1_request'),
        path('tutorial-2/', views.tutorial_2_request , name='tutorial_2_request'),
        path('tutorial-3/', views.tutorial_3_request , name='tutorial_3_request')
    ]))
]
