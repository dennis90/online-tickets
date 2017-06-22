from django.db import models


class Event(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.title


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    available_tickets = models.SmallIntegerField()
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="tickets",
        related_query_name="ticket"
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
