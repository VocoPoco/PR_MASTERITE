from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sys
import mysql.connector

sys.path.append("../DB")
from DB import User


class handleRegister():
    def __init__(self, request):
        self.request = request
    
    @csrf_exempt
    def register(self):
        if self.request.method == 'POST':
            first = self.request.POST.get('first', '')
            last = self.request.POST.get('last', '')
            email = self.request.POST.get('email', '')
            password = self.request.POST.get('password', '')
            
            cnx = mysql.connector.connect(user='root', host='127.0.0.0', database='User')
            cursor = cnx.cursor()
            insert_query = "INSERT INTO User SET first = %s, last  = %s, email = %s, password = %s"
            cursor.execute(insert_query, (first, last, email, password))
            user = cursor.fetchone()

            login(self.request, user)
            
            return JsonResponse({'email': user.email})
        else:
            return JsonResponse({'message': 'Invalid request method'}, status=405)
