from django.forms import ModelForm
from .models import Event, Category, Account
from django import forms

class DateInput(forms.DateInput):
  input_type = 'date'

class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['host']
        widgets = {
          'start_time': DateInput(),
        }


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = [
            'first_name',
            'surname',
            'email'
        ]