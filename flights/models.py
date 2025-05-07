import string
import random

from django.contrib.auth.models import User
from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} ({self.city})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.IntegerField(help_text="Duration in minutes")
    capacity = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin.code} to {self.destination.code}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.available_seats = self.capacity
        super().save(*args, **kwargs)

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

def generate_booking_code():
    chars = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(random.choices(chars, k=6))
        if not Booking.objects.filter(booking_code=code).exists():
            return code

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_code = models.CharField(max_length=6, unique=True, editable=False, default=generate_booking_code)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.flight.available_seats = self.flight.capacity - self.flight.booking_set.count()
        self.flight.save()

    def __str__(self):
        return f"Booking {self.booking_code} - {self.passenger.name}"