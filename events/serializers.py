from rest_framework import serializers
from .models import EventItem   


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventItem
        fields = '__all__'          