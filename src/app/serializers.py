from rest_framework import serializers

from app.models import Device, Reading


class DeviceSerializer(serializers.ModelSerializer[Device]):
    class Meta:
        model = Device
        fields = ["id", "name", "location", "created_at"]
        read_only_fields = ["id", "created_at"]


class ReadingSerializer(serializers.ModelSerializer[Reading]):
    device_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Reading
        fields = ["device_id", "observed_at", "temperature_c"]
