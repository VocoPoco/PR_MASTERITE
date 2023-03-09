from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class handleRegister():
    def __init__(self, request):
        self.request = request
    
    @csrf_exempt
    def register(self):
        if self.request.method == 'POST':
            form = UserCreationForm(self.request.POST)
            if form.is_valid():
                user = form.save()
                login(self.request, user)
                return JsonResponse({'message': 'User registered and logged in successfully'})
            else:
                return JsonResponse({'message': 'Error registering user'}, status=400)

        return JsonResponse({'message': 'Invalid request method'}, status=405)
