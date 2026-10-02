from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=200, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Reading(models.Model):
    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, related_name="readings"
    )
    observed_at = models.DateTimeField()
    temperature_c = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ["-observed_at"]

    def __str__(self) -> str:
        return f"{self.device.name} @ {self.observed_at.isoformat()}"
