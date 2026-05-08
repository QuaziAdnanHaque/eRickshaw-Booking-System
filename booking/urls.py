from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [

    path(
        'create/',
        views.create_ride,
        name='create_ride'
    ),

    path(
        'available/',
        views.available_rides,
        name='available_rides'
    ),

    path(
        'accept/<int:ride_id>/',
        views.accept_ride,
        name='accept_ride'
    ),
]