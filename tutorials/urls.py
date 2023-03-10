from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    # path('', views.about , name='about'),
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register')
    # path('', views.tutorial_1, name='tutorial_1'),
    # path('', views.tutorial_2 , name='tutorial_2'),
    # path('', views.tutorial_3 , name='tutorial_3'),
]
