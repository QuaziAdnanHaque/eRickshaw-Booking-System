from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . forms import RideForm
from . models import Ride

# Create your views here.

farePerKm = 10

@login_required
def create_ride(request):
    form = RideForm()
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.customer = request.user
            ride.fare = ride.distance * farePerKm
            ride.save()
            return redirect('accounts:customer_dashboard')
        else:
            print(form.errors)
    return render(request, 'booking/create_ride.html', {'form': form})
    
    
@login_required
def available_rides(request):
    rides = Ride.objects.filter(status='requested').order_by('-created_at')
    return render(request, 'booking/available_rides.html', {'rides': rides})


@login_required
def accept_ride(request, ride_id):
    ride = Ride.objects.get(id = ride_id)
    if ride.status == 'requested':
        ride.driver = request.user
        ride.status = 'accepted'
        ride.save()
    return redirect('booking:accepted_rides')

@login_required
def accepted_rides(request):
    rides = Ride.objects.filter(driver=request.user).order_by('-created_at')
    return render(request, 'booking/accepted_rides.html',{'rides': rides})

@login_required
def complete_ride(request, ride_id):
    if request.method == 'POST':
        ride = Ride.objects.get(id= ride_id, driver = request.user)
        if ride.status == 'accepted':
            ride.status = 'completed'
            ride.save()
        return redirect('booking:accepted_rides')
    
@login_required
def ride_history(request):

    rides = Ride.objects.filter(customer=request.user).order_by('-created_at')

    return render(request, 'booking/ride_history.html', {'rides': rides})
    
@login_required
def ride_history(request):

    rides = Ride.objects.filter( customer=request.user).order_by('-created_at')

    return render(request, 'booking/ride_history.html', {'rides': rides})