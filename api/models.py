from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class ApiUser(AbstractUser):
    ...



class Hotel(models.Model):
    name = models.CharField(max_length=128)


class Room(models.Model):
    num = models.PositiveIntegerField()
    hotel = models.ForeignKey(
        'api.Hotel',
        related_name='rooms',
        on_delete=models.CASCADE
    )


class Booking(models.Model):
    room = models.ForeignKey(
        'api.Room',
        related_name='bookings',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        'api.ApiUser',
        related_name='bookings',
        on_delete=models.CASCADE
    )
