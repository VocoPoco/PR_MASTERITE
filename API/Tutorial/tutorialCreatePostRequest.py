from django.contrib.auth import login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import mysql.connector
from rest_framework.viewsets import ModelViewSet


class TutorialCreate():
    @staticmethod
    @csrf_exempt
    def as_view():
        def register(request):
            if request.method == 'POST':
                name = request.POST.get('name', '')
                level = request.POST.get('level', '')
                description = request.POST.get('description', '')
                order = request.POST.get('order', '')

                cnx = mysql.connector.connect(user='root', host='localhost', database='Tutorial')
                cursor = cnx.cursor()
                edit_query = "INSERT INTO Tutorial SET `name` = %s, `level` = %s, `description` = %s, `order` = %s"
                cursor.execute(edit_query, (name, level, description, order))
                cnx.commit()

                return JsonResponse({'name': name})
            else:
                return JsonResponse({'message': 'Invalid request method'}, status=405)
        return register