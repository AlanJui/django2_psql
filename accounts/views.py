from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect

from .forms import RegisterForm, CustomUserCreationForm

# Create your views here.
class SignUpView(FormView):
    # form_class = UserCreationForm
    form_class = RegisterForm
    template_name = 'accounts/signup.html'
    success_url = 'login'

    def form_valid(self, form):
        """
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        """
        return super().form_valid(form)

# class SignUpView(generic.CreateView):
#     # form_class = UserCreationForm
#     form_class = RegisterForm
#     template_name = 'signup.html'
#     success_url = reverse_lazy('login')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {
        'form': form
    })