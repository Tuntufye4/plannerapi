from rest_framework import serializers
from .models import MonthlyTask   

class MonthlyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyTask
        fields = '__all__'                 