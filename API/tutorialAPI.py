from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import mysql.connector
from Tutorial.tutorial import Tutorial


@api_view(['GET'])
def ping():
    return JsonResponse({'message': 'bong'})

@api_view(['POST'])
def tutorial_edit(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        level = request.POST.get('level', '')
        description = request.POST.get('description', '')
        order = request.POST.get('order', '')
        tutorial_id = request.POST.get('id', '')

        cnx = mysql.connector.connect(user='root', host='localhost', database='Tutorial')
        cursor = cnx.cursor()
        update_query = "UPDATE Tutorial SET name = %s, level = %s, description = %s, order = %s WHERE id = %s"
        cursor.execute(update_query, (name, level, description, order, tutorial_id))
        cnx.commit()

        return JsonResponse({'message': 'Tutorial updated successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)

@api_view(['POST'])
def tutorial_create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        level = request.POST.get('level', '')
        description = request.POST.get('description', '')
        order = request.POST.get('order', '')

        tutorial = Tutorial(name=name, level=level, description=description, order=order)
        tutorial.save()

        return Response({'name': name})
    else:
        return Response({'message': 'Invalid request method'}, status=405)