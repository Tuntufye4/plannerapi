from rest_framework import viewsets
from .models import  EventItem   
from .serializers import EventSerializer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = EventItem.objects.all().order_by('-created_at')
    serializer_class = EventSerializer               