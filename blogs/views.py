from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm

# Create your views here.
class PostListView(ListView):
    model = Post

class PostDetailView(View):
    form_class = PostForm
    template_name = 'blogs/post_detail.html'

    def get(self, request, *args, **kwargs):
        object = get_object_or_404(Post, pk=kwargs['pk'])
        form = self.form_class(instance=object)
        return render(request, self.template_name, {
            'form': form,
            'form_title': 'Detail of Post',
            'object': object,
        })

class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('post-list')

class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('post-list')
    # fields = [
    #     'title',
    #     'text'
    # ]

class PostDeleteView(DeleteView):
    model = Post
    fields = '__all__'
    template_name = 'blogs/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def get(self, request, *args, **kwargs):
        object = get_object_or_404(Post, pk=kwargs['pk'])
        form = PostForm(instance=object)
        return render(request, self.template_name, {
            'form': form,
            'object': object,
        })
