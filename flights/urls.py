from django.contrib.auth.views import LogoutView
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'flights'
urlpatterns = [
    path('api/', include([
    path('api-token-auth/', obtain_auth_token),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('', views.IndexAPIView.as_view(), name='index'),
    path('flight/<int:flight_id>/', views.FlightDetailAPIView.as_view(), name='flight_detail'),
    path('airport/<str:airport_code>/', views.AirportDetailAPIView.as_view(), name='airport_detail'),
    path('flight/bookings/', views.BookFlightAPIView.as_view(), name='book_flight'),
    path('booking/<str:booking_code>/', views.BookingConfirmationAPIView.as_view(), name='booking_confirmation'),
    path('manage-booking/', views.ManageBookingAPIView.as_view(), name='manage_booking'),
    path('profile/', views.ProfileAPIView.as_view(), name='profile'),

    ])),
]


