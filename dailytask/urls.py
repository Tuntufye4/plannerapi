from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DailyTaskViewSet

router = DefaultRouter()
router.register(r'', DailyTaskViewSet, basename='daily-tasks')

urlpatterns = router.urls         