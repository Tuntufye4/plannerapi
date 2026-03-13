from rest_framework import viewsets
from .models import DailyTask
from .serializers import DailyTaskSerializer   


class DailyTaskViewSet(viewsets.ModelViewSet):
    queryset = DailyTask.objects.all().order_by('-created_at')
    serializer_class = DailyTaskSerializer            