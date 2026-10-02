from typing import Any

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Device
from app.serializers import DeviceSerializer


class HealthView(APIView):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return Response({"status": "ok"})


class DeviceViewSet(viewsets.ModelViewSet[Device]):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
