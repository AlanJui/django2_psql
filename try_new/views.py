from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Person
from .forms import ContactForm, PersonForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'try_new/home.html', {
        'form': form
    })

class PersonDetailView(DetailView):
    model = Person
    template_name = 'try_new/person_form.html'

def list_person(request):
    persons = Person.objects.all()
    return render(request, 'try_new/list_person.html', {
        'persons': persons
    })

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            return redirect('list_person')
    else:
        form = PersonForm()
    return render(request, 'try_new/add_person.html', {
        'form': form
    })