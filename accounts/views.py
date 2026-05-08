from django.shortcuts import render, redirect
from django.contrib.auth import  login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .models import Profile
from booking.models import Ride

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)
            profile.user_type = form.cleaned_data['user_type']
            profile.save()
            print("USER SAVED:", user.username, profile.user_type)
            return redirect('login')
        else:
            print("FORM ERRORS:", form.errors)
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def customer_dashboard(request):

    rides = Ride.objects.filter(
        customer=request.user
    ).order_by('-created_at')

    return render(
        request,
        'accounts/customer_dashboard.html',
        {
            'rides': rides
        }
    )

@login_required
@login_required
def driver_dashboard(request):

    rides = Ride.objects.filter(
        driver=request.user
    ).order_by('-created_at')

    accepted_count = rides.count()

    return render(
        request,
        'accounts/driver_dashboard.html',
        {
            'rides': rides,
            'accepted_count': accepted_count
        }
    )

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            elif user.profile.user_type == 'driver':
                return redirect(
                    'accounts:driver_dashboard'
                )
            else:
                return redirect('accounts:customer_dashboard')
    return render(request, 'registration/login.html', {'form': form})