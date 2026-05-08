from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name= 'register'),
    path('customer/', views.customer_dashboard, name='customer_dashboard'),
    path('driver/', views.driver_dashboard, name='driver_dashboard'),
]
