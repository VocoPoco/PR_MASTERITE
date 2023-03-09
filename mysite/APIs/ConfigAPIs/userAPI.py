from rest_framework.decorators import api_view
from django.http import JsonResponse
import mysql.connector


@api_view(['GET'])
def ping():
    return JsonResponse({'message': 'cong'})

@api_view(['POST'])
def user_edit(request):
    if request.method == 'POST':
        first = request.POST.get('first', '')
        last = request.POST.get('last', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        cnx = mysql.connector.connect(user='root', host='localhost', database='User')
        cursor = cnx.cursor()
        update_query = "UPDATE User SET first = %s, last = %s, email = %s, password = %s WHERE id = %s"
        cursor.execute(update_query, (first, last, email, password))
        cnx.commit()

        return JsonResponse({'message': 'Account updated successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)