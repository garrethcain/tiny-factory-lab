import pytest
from rest_framework.test import APIClient

from app.models import Device


@pytest.mark.django_db
def test_create_device_returns_201():
    client = APIClient()

    response = client.post(
        "/api/devices/",
        {"name": "esp32-lab", "location": "bench"},
        format="json",
    )

    assert response.status_code == 201
    assert response.json()["name"] == "esp32-lab"
    assert response.json()["location"] == "bench"


@pytest.mark.django_db
def test_list_devices_returns_created_devices():
    Device.objects.create(name="sensor-01", location="greenhouse")
    client = APIClient()

    response = client.get("/api/devices/")

    assert response.status_code == 200
    assert [item["name"] for item in response.json()] == ["sensor-01"]
