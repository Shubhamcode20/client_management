from django.db import models
from django.contrib.auth.models import User

class ClientProfile(models.Model):
    name = models.CharField(max_length=255)
    primary_number = models.CharField(max_length=20)
    country_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    appointment_datetime = models.DateTimeField()
    account_holder_id = models.IntegerField()
    status = models.CharField(max_length=10, choices=[('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')])
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment with {self.client.name} on {self.appointment_datetime}"
