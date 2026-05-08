from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .models import Profile

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Ensure profile exists
            profile, created = Profile.objects.get_or_create(user=user)

            # Set role
            profile.user_type = form.cleaned_data['user_type']
            profile.save()

            print("USER SAVED:", user.username, profile.user_type)  # debug

            return redirect('login')

        else:
            print("FORM ERRORS:", form.errors)  # 🔥 THIS WILL TELL YOU EVERYTHING

    return render(request, 'accounts/register.html', {'form': form})

@login_required
def customer_dashboard(request):
    return render(request, 'accounts/customer_dashboard.html')

@login_required
def driver_dashboard(request):
    return render(request, 'accounts/driver_dashboard.html')

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            # role-based redirect
            if user.profile.user_type == 'driver':
                return redirect('accounts:driver_dashboard')

            return redirect('accounts:customer_dashboard')

        else:
            return render(request, 'registration/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'registration/login.html')