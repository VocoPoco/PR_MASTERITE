from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import mysql.connector



class Login():
    def __init__(self):
        self.request = None

    @csrf_exempt
    def login(self, request):
        self.request = request
        if self.request.method == 'POST':
            email = self.request.POST.get('email', '')
            password = self.request.POST.get('password', '')

            cnx = mysql.connector.connect(user='root', host='127.0.0.0', database='User')
            cursor = cnx.cursor()
            select_query = "SELECT * FROM User WHERE email = %s AND password = %s"
            cursor.execute(select_query, (email, password))
            user = cursor.fetchone()

            if user is not None:
                account_user = authenticate(self.request, username=user[3], password=user[4])
                if account_user is not None:
                    login(self.request, account_user)
                    return JsonResponse({'email': account_user.email})
                else:
                    return JsonResponse({'message': 'Invalid login credentials'}, status=400)
            else:
                return JsonResponse({'message': 'Invalid login credentials'}, status=400)

        return JsonResponse({'message': 'Invalid request method'}, status=405)