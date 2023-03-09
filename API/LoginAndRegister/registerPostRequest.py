from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sys
import mysql.connector


class Register():
    def __init__(self):
        pass
    
    @csrf_exempt
    def register(self, request):
        if request.method == 'POST':
            first = request.POST.get('first', '')
            last = request.POST.get('last', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            
            cnx = mysql.connector.connect(user='root', host='127.0.0.0', database='User')
            cursor = cnx.cursor()
            insert_query = "INSERT INTO User (first, last, email, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (first, last, email, password))
            cnx.commit()

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({'email': user.email})
            else:
                return JsonResponse({'message': 'Invalid email or password'}, status=401)
        else:
            return JsonResponse({'message': 'Invalid request method'}, status=405)