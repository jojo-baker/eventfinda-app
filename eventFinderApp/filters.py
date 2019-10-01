import django_filters
from .models import Event
from django.contrib.auth.models import Group
from django import forms
from django.forms import ModelForm, SplitDateTimeField
from django.contrib.admin import widgets

class EventFilter(django_filters.FilterSet):
    start_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())
        
    class Meta:
        model = Event
        fields = ('categories', 'location', 'start_time')
        