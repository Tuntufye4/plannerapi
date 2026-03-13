from rest_framework import serializers
from .models import WeeklyTask   

class WeeklyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyTask
        fields = '__all__'                