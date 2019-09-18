from django.forms import ModelForm
from .models import Event, Category, Account

class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['host']


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = [
            'first_name',
            'surname',
            'email'
        ]