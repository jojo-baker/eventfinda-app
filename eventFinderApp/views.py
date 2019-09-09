from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import Event, Account
from .forms import EventForm, AccountForm

class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()


class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'

class AccountView(generic.DetailView):
    model = Account
    template_name = 'eventFinderApp/account.html'

def account(request):
    accountform = AccountForm()
    return render(request, 'eventFinderApp/account.html', {'accountform': accountform})

def add_event(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
            form.save()
            return HttpResponseRedirect(reverse('eventFinderApp:index'))
        return render(request, 'eventFinderApp/add-event.html', {'eventform': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        eventform = EventForm()
        return render(request, 'eventFinderApp/add-event.html', {'eventform': eventform})