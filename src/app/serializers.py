from rest_framework import serializers

from app.models import Device


class DeviceSerializer(serializers.ModelSerializer[Device]):
    class Meta:
        model = Device
        fields = ["id", "name", "location", "created_at"]
        read_only_fields = ["id", "created_at"]
