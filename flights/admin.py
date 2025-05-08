from django.contrib import admin
from django.contrib.auth.models import User
from .models import Booking, Passenger

class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0

class PassengerAdmin(admin.ModelAdmin):
    inlines = [BookingInline]

admin.site.register(Passenger, PassengerAdmin)
