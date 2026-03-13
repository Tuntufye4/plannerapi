from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MonthlyTaskViewSet

router = DefaultRouter()
router.register(r'', MonthlyTaskViewSet, basename='monthly-tasks')

urlpatterns = router.urls               