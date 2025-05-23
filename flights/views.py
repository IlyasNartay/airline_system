from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Count
from .models import Airport, Flight, Booking, Passenger
from .serializers import (
    RegisterSerializer, AirportSerializer, FlightSerializer,
    BookingSerializer, BookingManageSerializer, UserSerializer,
)
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration successful."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class IndexAPIView(APIView):
    def get(self, request):
        airports = Airport.objects.annotate(
            total_flights=Count('departures') + Count('arrivals')
        ).order_by('-total_flights')
        flights = Flight.objects.all()
        return Response({
            'airports': AirportSerializer(airports, many=True).data,
            'flights': FlightSerializer(flights, many=True).data,
        })
class FlightDetailAPIView(APIView):
    def get(self, request, flight_id):
        flight = get_object_or_404(Flight, pk=flight_id)
        bookings = flight.booking_set.all()
        booked_seats = bookings.count()
        available_seats = flight.capacity - booked_seats
        return Response({
            'flight': FlightSerializer(flight).data,
            'bookings': BookingSerializer(bookings, many=True).data,
            'available_seats': available_seats
        })
class BookFlightAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        flight_id = request.data.get('flight_id')
        name = request.data.get('name')
        email = request.data.get('email')
        user = request.user
        print(request)
        try:
            flight = Flight.objects.get(id=flight_id)
        except Flight.DoesNotExist:
            return Response({'error': 'Flight not found.'}, status=status.HTTP_404_NOT_FOUND)
        if flight.booking_set.count() >= flight.capacity:
            return Response({'error': 'No available seats.'}, status=status.HTTP_400_BAD_REQUEST)
        passenger, created = Passenger.objects.get_or_create(
            email=email,
            defaults={'name': name}
        )
        booking = Booking.objects.create(user = user,passenger=passenger, flight=flight)
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class BookingConfirmationAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, booking_code):
        booking = get_object_or_404(Booking, booking_code=booking_code)
        return Response(BookingSerializer(booking).data)
class ManageBookingAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = BookingManageSerializer(data=request.data)
        if serializer.is_valid():
            booking_code = serializer.validated_data['booking_code']
            try:
                booking = Booking.objects.select_related('passenger', 'flight').get(booking_code=booking_code)
                return Response(BookingSerializer(booking).data)
            except Booking.DoesNotExist:
                return Response({"error": "Invalid booking code."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AirportDetailAPIView(APIView):
    def get(self, request, airport_code):
        airport = get_object_or_404(Airport.objects.prefetch_related('departures', 'arrivals'), code=airport_code)
        departures = airport.departures.annotate(booked_seats=Count('booking'))
        arrivals = airport.arrivals.annotate(booked_seats=Count('booking'))
        return Response({
            'airport': AirportSerializer(airport).data,
            'departures': FlightSerializer(departures, many=True).data,
            'arrivals': FlightSerializer(arrivals, many=True).data,
        })
class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        bookings = Booking.objects.filter(user=user)
        return Response({
            'bookings': BookingSerializer(bookings, many=True).data,
            'user' : {
                'username' : user.username,
                'email' : user.email,
            }
        })
class AdminUserListAPIView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        try:
            users = User.objects.filter(is_superuser=False)
            user_data = []
            for user in users:
                bookings = Booking.objects.filter(user=user)
                serialized_bookings = BookingSerializer(bookings, many=True).data
                serialized_user = UserSerializer(user).data
                user_data.append({
                    "user": serialized_user,
                    "bookings": serialized_bookings
                })
            return Response({'data': user_data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class AdminUserUpdateAPIView(APIView):
    permission_classes = [IsAdminUser]
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({'message': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)
class AddUserAPIView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration successful."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserInfoAPIView(APIView):
    def get(self, request):
        return Response({'users' : UserSerializer(request.user).data})