from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime, timezone
User = get_user_model()

class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    categories = models.ManyToManyField('Category', related_name='events')
    event_description = models.TextField(max_length=600, default = 'Description')
    host = models.ForeignKey(User, related_name = 'hosting_events', on_delete=models.DO_NOTHING)
       
    def __str__(self):
        return self.title

    def is_past_event(self):
        return self.start_time < datetime.now(tz = timezone.utc)   



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Account(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()

