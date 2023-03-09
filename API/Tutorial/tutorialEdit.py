from django.contrib.auth import login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import mysql.connector


class TutorialEdit():
    def __init__(self, request):
        self.request = request
    
    @csrf_exempt
    def register(self):
        if self.request.method == 'POST':
            name = self.request.POST.get('name', '')
            level = self.request.POST.get('level', '')
            description = self.request.POST.get('description', '')
            order = self.request.POST.get('order', '')
            
            cnx = mysql.connector.connect(user='root', host='127.0.0.0', database='Tutorial')
            cursor = cnx.cursor()
            update_query = "UPDATE Tutorial SET name = %s, level = %s, description = %s, order = %s WHERE id = %s"
            cursor.execute(update_query, (name, level, description, order))
            tutorial = cursor.fetchone()
            
            return JsonResponse({'name': tutorial.name})
        else:
            return JsonResponse({'message': 'Invalid request method'}, status=405)