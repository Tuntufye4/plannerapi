from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ShoppingViewSet

router = DefaultRouter()
router.register(r'', ShoppingViewSet, basename='shopping-tasks')

urlpatterns = router.urls                  