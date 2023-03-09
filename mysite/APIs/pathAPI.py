from django.urls import path
from . import loginAPI, progressAPI, tutorialAPI, userAPI 

class Paths():
    def __init__(self):
        self.login = loginAPI()
        self.progress = progressAPI()
        self.tutorial = tutorialAPI()
        self.user = userAPI()

        self.urlpatterns = [
                path('ping/', self.login.ping, name='ping'),
                path('login/', self.login.login, name='login'),
                path('register/', self.login.register , name='register'),
                path('tutorial_edit/', self.tutorial.tutorial_edit, name='tutorial_edit'),
                path('tutorial_create/', self.tutorial.tutorial_create, name='tutorial_create'),
                path('user_edit/', self.user.user_edit , name='user_edit'),
                # path('register/', self.progress.register , name='register'),
                # path('register/', self.progress.register , name='register'),
                # path('register/', self.progress.register , name='register'),
        ]