from django.contrib import admin
from .models import Passenger, Airport, Flight, Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_code', 'passenger', 'flight', 'created_at')
    search_fields = ('booking_code', 'passenger__name')
    list_filter = ('flight', 'created_at')

admin.site.register(Passenger)
admin.site.register(Airport)
admin.site.register(Flight)
