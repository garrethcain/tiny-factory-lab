from app.models import Device, Reading


def list_device_readings(device: Device) -> list[Reading]:
    return list(device.readings.all())
