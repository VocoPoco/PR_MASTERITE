from django.contrib.auth import login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import mysql.connector


class TutorialEdit():
    def __call__(self, request):
        if request.method == 'POST':
            name = request.POST.get('name', '')
            level = request.POST.get('level', '')
            description = request.POST.get('description', '')
            order = request.POST.get('order', '')
            
            cnx = mysql.connector.connect(user='root', host='127.0.0.0', database='Tutorial')
            cursor = cnx.cursor()
            update_query = "UPDATE Tutorial SET name = %s, level = %s, description = %s, order = %s WHERE id = %s"
            cursor.execute(update_query, (name, level, description, order))
            cnx.commit()
            
            return JsonResponse({'message': 'Tutorial updated successfully'})
        else:
            return JsonResponse({'message': 'Invalid request method'}, status=405)