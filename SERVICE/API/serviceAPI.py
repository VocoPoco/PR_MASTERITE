from django.urls import path
from SERVICE.handleLogin import *
from SERVICE.handleRegister import *


class API():
    def __init__(self):
        self.login = handleLogin()
        self.register = handleRegister()
        
        self.url_register = [
            path('api/register/', self.register.register, name='register'),
        ]
        self.url_login = [
            path('api/login/', self.login.login, name='login'),
        ]