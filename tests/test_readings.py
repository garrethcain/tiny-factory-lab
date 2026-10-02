from datetime import timedelta

import pytest
from django.utils import timezone
from rest_framework.test import APIClient

from app.models import Device, Reading


def make_reading(device: Device, minutes_ago: int, temperature: str) -> Reading:
    return Reading.objects.create(
        device=device,
        observed_at=timezone.now() - timedelta(minutes=minutes_ago),
        temperature_c=temperature,
    )


@pytest.mark.django_db
def test_readings_newest_first():
    client = APIClient()
    device = Device.objects.create(name="sensor-01", location="greenhouse")
    make_reading(device, minutes_ago=30, temperature="20.50")
    make_reading(device, minutes_ago=5, temperature="21.75")
    make_reading(device, minutes_ago=60, temperature="19.25")

    response = client.get(f"/api/devices/{device.id}/readings/")

    assert response.status_code == 200
    temps = [item["temperature_c"] for item in response.json()]
    assert temps == ["21.75", "20.50", "19.25"]


@pytest.mark.django_db
def test_readings_include_device_id_observed_at_and_temperature_c():
    client = APIClient()
    device = Device.objects.create(name="sensor-01")
    reading = make_reading(device, minutes_ago=1, temperature="22.00")

    response = client.get(f"/api/devices/{device.id}/readings/")

    assert response.status_code == 200
    item = response.json()[0]
    assert set(item) == {"device_id", "observed_at", "temperature_c"}
    assert item["device_id"] == device.id
    assert item["observed_at"] == reading.observed_at.isoformat().replace("+00:00", "Z")
    assert item["temperature_c"] == "22.00"


@pytest.mark.django_db
def test_readings_exclude_other_devices():
    client = APIClient()
    mine = Device.objects.create(name="sensor-01")
    other = Device.objects.create(name="sensor-02")
    make_reading(mine, minutes_ago=5, temperature="20.00")
    make_reading(other, minutes_ago=3, temperature="99.99")
    make_reading(other, minutes_ago=1, temperature="88.88")

    response = client.get(f"/api/devices/{mine.id}/readings/")

    assert response.status_code == 200
    items = response.json()
    assert len(items) == 1
    assert items[0]["device_id"] == mine.id
    assert items[0]["temperature_c"] == "20.00"


@pytest.mark.django_db
def test_readings_unknown_device_returns_404():
    client = APIClient()

    response = client.get("/api/devices/9999/readings/")

    assert response.status_code == 404


@pytest.mark.django_db
def test_readings_empty_history_returns_empty_list():
    client = APIClient()
    device = Device.objects.create(name="sensor-01")

    response = client.get(f"/api/devices/{device.id}/readings/")

    assert response.status_code == 200
    assert response.json() == []
