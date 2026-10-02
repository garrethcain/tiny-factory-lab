from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app import views

router = DefaultRouter()
router.register("devices", views.DeviceViewSet, basename="device")

urlpatterns = [
    path("healthz/", views.HealthView.as_view(), name="health"),
    path("", include(router.urls)),
]
