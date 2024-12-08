from django.db import models
from django.contrib.auth.models import User  # Import the User model 

class Driver(models.Model):  
    driver_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key  
    first_name = models.CharField(max_length=50)  
    last_name = models.CharField(max_length=50)  
    driving_license = models.CharField(max_length=50) 
    email = models.EmailField(unique=True)  
    phone = models.CharField(unique=True, max_length=25)  
    class Meta:  
        db_table = "drivers"

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    plate_number = models.CharField(unique=True, max_length=20)  # Added max_length
    model = models.CharField(max_length=50)  # Added max_length
    year = models.IntegerField()
    color = models.CharField(max_length=30)
    transmission = models.CharField(max_length=20)
    cost_per_day = models.IntegerField()
    driver_id = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, default='Available')  # Added max_length
    class Meta:
        db_table = "cars"

class Booking(models.Model):  
    booking_id = models.AutoField(primary_key=True)  
    booking_date = models.DateField()
    return_date = models.DateField()
    total_cost = models.IntegerField() 
    car_id = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True)
    client_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20)  # Added max_length
    class Meta:  
        db_table = "bookings"