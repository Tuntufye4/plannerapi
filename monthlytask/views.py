from rest_framework import viewsets
from .models import MonthlyTask
from .serializers import MonthlyTaskSerializer   


class MonthlyTaskViewSet(viewsets.ModelViewSet):
    queryset = MonthlyTask.objects.all().order_by('-created_at')
    serializer_class = MonthlyTaskSerializer          