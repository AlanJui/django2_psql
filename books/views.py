from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Publisher, Author

from .forms import AuthorForm

class PublisherListView(ListView):
    model = Publisher
    template_name = 'books/publisher_list.html'

# ------------------------------------------------

class AuthorListView(ListView):
    model = Author

class AuthorDetailView(View):
    form_class = AuthorForm
    template_name = 'books/author_detail.html'
    success_url = reverse_lazy('author-list')

    def get(self, request, *args, **kwargs):
        object = get_object_or_404(Author, pk=kwargs['pk'])
        form = self.form_class(instance=object)
        return render(request, self.template_name, {
            'form': form,
            'form_title': 'Detail of Author',
            'object': object,
        })

    # def get_object(self, *args, **kwargs):
    #     object = get_object_or_404(Author, pk=self.kwargs[ 'pk' ])
    #     return object

    # def get_success_url(self):
    #     return reverse_lazy('author-list')

class AuthorCreateView(CreateView):
    model = Author
    fields = '__all__'
    template_name = 'books/author_form.html'
    success_url = reverse_lazy('author-list')

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name, { 'form': form })
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         # return HttpResponseRedirect('/books/author/')
    #         author = form.save()
    #         return redirect('author-list')
    #     return render(request, self.template_name, { 'form': form })

class AuthorUpdateView(UpdateView):
    model = Author
    fields = '__all__'
    template_name = 'books/author_update_form.html'
    success_url = reverse_lazy('author-list')

class AuthorDeleteView(DeleteView):
    model = Author
    fields = '__all__'
    template_name = 'books/author_confirm_delete.html'
    success_url = reverse_lazy('author-list')

    def get(self, request, *args, **kwargs):
        object = get_object_or_404(Author, pk=kwargs['pk'])
        form = AuthorForm(instance=object)
        return render(request, self.template_name, {
            'form': form,
            'object': object,
        })

