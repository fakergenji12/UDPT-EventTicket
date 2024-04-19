from django.db import models

class Tickets(models.Model):
    tickerId = models.AutoField(primary_key=True)
    eventId = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ticketType = models.CharField(max_length=50)
    availableSeats = models.IntegerField()
