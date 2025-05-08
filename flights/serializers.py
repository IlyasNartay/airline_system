from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Airport, Flight, Booking, Passenger


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    origin = serializers.CharField(source='origin.code', read_only=True)
    destination = serializers.CharField(source='destination.code', read_only=True)

    class Meta:
        model = Flight
        fields = ['id', 'origin', 'destination', 'duration', 'capacity', 'available_seats']


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(read_only=True)
    flight = FlightSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'



class BookingManageSerializer(serializers.Serializer):
    booking_code = serializers.CharField(max_length=10)

    def validate_booking_code(self, value):
        if not Booking.objects.filter(booking_code=value).exists():
            raise serializers.ValidationError("Booking not found.")
        return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'date_joined']