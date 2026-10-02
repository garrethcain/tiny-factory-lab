from typing import Any

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Device
from app.serializers import DeviceSerializer, ReadingSerializer
from app.services import readings as reading_services


class HealthView(APIView):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return Response({"status": "ok"})


class DeviceViewSet(viewsets.ModelViewSet[Device]):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    @action(detail=True, methods=["get"])
    def readings(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        device = self.get_object()
        device_readings = reading_services.list_device_readings(device)
        serializer = ReadingSerializer(device_readings, many=True)
        return Response(serializer.data)
