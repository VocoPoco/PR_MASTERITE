from rest_framework import serializers
from Tutorial.tutorial import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial()
        fields = ['id', 'name', 'level', 'description', 'order']