from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import WeeklyTaskViewSet

router = DefaultRouter()
router.register(r'', WeeklyTaskViewSet, basename='weekly-tasks')

urlpatterns = router.urls                