from django.urls import path
from Tutorial.tutorialCreatePostRequest import *
from Tutorial.tutorialEditPostRequest import *


class API():
    def __init__(self):
        self.tutorial_create = TutorialCreate()
        self.tutorial_edit = TutorialEdit()
        
        self.url_ping = [
            path('api/ping', self.ping, name='ping'),
        ]
        self.url_edit = [
            path('api/tutorial_edit', self.tutorial_edit, name='tutorial_edit')
        ]

        self.url_create = [
            path('api/tutorial_create', self.tutorial_create, name='tutorial_create')
        ]

    def ping(self):
        return JsonResponse({'message': 'pong'})