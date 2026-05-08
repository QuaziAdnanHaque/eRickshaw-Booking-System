from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ride(models.Model):
    Status_Choice = (
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
    )
    customer = models.ForeignKey(User, on_delete= models.CASCADE, related_name='customer_rides')
    driver = models.ForeignKey(User, on_delete= models.SET_NULL, null= True, blank= True, related_name= 'driver_rides')
    pickup = models.CharField(max_length= 255)
    drop = models.CharField(max_length= 255)
    distance = models.FloatField()
    fare = models.FloatField()
    status = models.CharField(max_length= 20, choices= Status_Choice, default= 'requested')
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.customer.username} - {self.pickup} -> {self.drop}" 