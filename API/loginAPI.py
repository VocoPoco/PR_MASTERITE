from django.urls import path
from LoginAndRegister.loginPostRequest import *
from LoginAndRegister.registerPostRequest import *


class API():
    def __init__(self):
        self.login = Login()
        self.register = Register()

        self.url_ping = [
            path('api/ping', "ping", name='ping'),
        ]
        self.url_register = [
            path('api/register/', self.register.register, name='register'),
        ]
        self.url_login = [
            path('api/login/', self.login.login, name='login'),
        ]