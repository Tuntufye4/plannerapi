from rest_framework import viewsets
from .models import WeeklyTask     
from .serializers import WeeklyTaskSerializer 


class WeeklyTaskViewSet(viewsets.ModelViewSet):
    queryset = WeeklyTask.objects.all().order_by('-created_at')
    serializer_class = WeeklyTaskSerializer                  