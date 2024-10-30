
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

class TableBooking(models.Model):
    customer_name = models.CharField(max_length=100)
    booking_time = models.DateTimeField()
    number_of_people = models.IntegerField()
