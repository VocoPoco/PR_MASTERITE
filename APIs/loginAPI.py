from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import mysql.connector
from LoginAndRegister.userSerializer import UserSerializer

@api_view(['GET'])
def ping():
    return JsonResponse({'message': 'pong'})

@api_view(['POST'])
@csrf_exempt
def login(request):
    email = request.data.get('email', '')
    password = request.data.get('password', '')

    cnx = mysql.connector.connect(user='root', host='127.0.0.0', database='User')
    cursor = cnx.cursor()
    select_query = "SELECT * FROM User WHERE email = %s AND password = %s"
    cursor.execute(select_query, (email, password))
    user = cursor.fetchone()

    if user is not None:
        account_user = authenticate(request, username=user[3], password=user[4])
        if account_user is not None:
            login(request, account_user)
            serializer = UserSerializer(account_user)
            if user[5] == '1':
                # admin interface
                return JsonResponse({'message': 'Welcome to the admin interface', 'data': serializer.data})
            else:
                # normal interface
                return JsonResponse({'message': 'Login successful', 'data': serializer.data})
        else:
            return JsonResponse({'message': 'Invalid login credentials'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid login credentials'}, status=400)


@api_view(['POST'])
@csrf_exempt
def register(request):
    first = request.data.get('first', '')
    last = request.data.get('last', '')
    email = request.data.get('email', '')
    password = request.data.get('password', '')

    cnx = mysql.connector.connect(user='root', host='127.0.0.0', database='User')
    cursor = cnx.cursor()
    insert_query = "INSERT INTO User (first, last, email, password) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (first, last, email, password))
    cnx.commit()

    user = authenticate(request, email=email, password=password)
# TO DO: Check if the "type" is 1 and if yes enter the admin interface (needs an admin interface to be created) 
    if user is not None:
        login(request, user)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    else:
        return JsonResponse({'message': 'Invalid email or password'}, status=401)