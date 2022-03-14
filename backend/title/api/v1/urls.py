from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import REviewViewSet

router = DefaultRouter()
router.register("review", REviewViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
