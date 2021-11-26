from rest_framework.serializers import ModelSerializer
from .models import Assignment

class AssignmentSerializer(ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

    