from django.db.models import QuerySet

from app.models import Device, Reading


def list_device_readings(device: Device) -> QuerySet[Reading]:
    return device.readings.all()
