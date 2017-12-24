from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from .models import Person, Author
from .forms import ContactForm, PersonForm

# Create your views here.
class PersonListView(ListView):
    model = Person

class PersonDetailView(View):
    form_class = PersonForm
    template_name = 'try_new/person_detail.html'

    def get(self, request, *args, **kwargs):
        object = get_object_or_404(Person, pk=kwargs['pk'])
        form = self.form_class(instance=object)
        return render(request, self.template_name, {
            'form': form,
            'form_title': 'Detail of Person',
            'object': object,
        })

class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('person-list')

class PersonUpdateView(UpdateView):
    model = Person
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('person-list')

class PersonDeleteView(DeleteView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('person-list')
    template_name = 'try_new/person_confirm_delete.html'

    def get(self, request, *args, **kwargs):
        object = get_object_or_404(Person, pk=kwargs['pk'])
        form = PersonForm(instance=object)
        return render(request, self.template_name, {
            'form': form,
            'object': object,
        })

#========================================================

class AuthorListView(ListView):
    model = Author
    # fields = ['first_name', 'last_name', 'email', 'phone', 'bio']
    # template_name = 'try_new/author_list.html'

class AuthorDetailView(DetailView):
    model = Author
    fields = ['first_name', 'last_name', 'email', 'phone', 'bio']
    template_name = 'try_new/author_detail.html'

class AuthorCreateView(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'email', 'phone', 'bio']
    template_name = 'try_new/author_form.html'

class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'email', 'phone', 'bio']

class AuthorDeleteView(DeleteView):
    model = Author
    fields = ['first_name', 'last_name', 'email', 'phone', 'bio']

    success_url = reverse_lazy('author_list')

# def home(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             pass # does nothing, just trigger the validation
#     else:
#         form = ContactForm()
#     return render(request, 'try_new/post_list.html', {
#         'form': form
#     })

# def list_person(request):
#     persons = Person.objects.all()
#     return render(request, 'try_new/list_person.html', {
#         'persons': persons
#     })
#
# def show_detail(request, pk):
#     object = get_object_or_404(Person, pk=pk)
#     form = PersonForm(instance=model)
#     return render(request, 'try_new/person_detail.html', {
#         'form': form,
#         'object': object
#     })
#
# def add_person(request):
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             person = form.save()
#             return redirect('list_person')
#     else:
#         form = PersonForm()
#     return render(request, 'try_new/add_person.html', {
#         'form': form
#     })

