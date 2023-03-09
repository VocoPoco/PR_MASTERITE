from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sys
import mysql.connector


class handleLogin():
    def __init__(self, request):
        self.request = request
    
    @csrf_exempt
    def login(self):
        if self.request.method == 'POST':
            username = self.request.POST.get('username', '')
            password = self.request.POST.get('password', '')

            cnx = mysql.connector.connect(user='root', host='127.0.0.0', database='User')
            cursor = cnx.cursor()
            select_query = "SELECT * FROM User WHERE email = %s AND password = %s"
            cursor.execute(select_query, (username, password))
            user = cursor.fetchone()

            if user is not None:
                account_user = authenticate(self.request, username=user[3], password=user[4])
                if account_user is not None:
                    login(self.request, account_user)
                    return JsonResponse({'username': account_user.username})
                else:
                    return JsonResponse({'message': 'Invalid login credentials'}, status=400)
            else:
                return JsonResponse({'message': 'Invalid login credentials'}, status=400)

        return JsonResponse({'message': 'Invalid request method'}, status=405)