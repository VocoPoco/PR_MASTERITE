from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sys
sys.path.append("..")
from DB.DB import User

class handleLogin():
    def __init__(self, request):
        self.request = request
    
    @csrf_exempt
    def login(self):
        if self.request.method == 'POST':
            username = self.request.POST.get('username', '')
            password = self.request.POST.get('password', '')
            user = authenticate(self.request, username=username, password=password)
            if user is not None:
                login(self.request, user)
                return JsonResponse({'username': user.username, 'password': password})
            else:
                return JsonResponse({'message': 'Invalid login credentials'}, status=400)

        return JsonResponse({'message': 'Invalid request method'}, status=405)