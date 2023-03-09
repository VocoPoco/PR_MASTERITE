from django.forms import ModelForm
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from Tutorial.tutorial import Tutorial
from Tutorial.tutorialSerializer import TutorialSerializer


class TutorialForm(ModelForm):
    class Meta():
        model = Tutorial()
        fields = ['name', 'level', 'description', 'order']


class TutorialViewSet(ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

    @action(methods=['post'], detail=False)
    def create_tutorial(self, request):
        form = TutorialForm(request.POST)
        if form.is_valid():
            tutorial = form.save()
            return Response({'name': tutorial.name})
        else:
            return Response(form.errors, status=400)

    @action(methods=['post'], detail=True)
    def update_tutorial(self, request, pk):
        tutorial = self.get_object()
        form = TutorialForm(request.POST, instance=tutorial)
        if form.is_valid():
            form.save()
            return Response({'message': 'Tutorial updated successfully'})
        else:
            return Response(form.errors, status=400)