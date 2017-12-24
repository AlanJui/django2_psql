from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect

from .forms import RegisterForm, CustomUserCreationForm

# Create your views here.
# class SignUpView(FormView):
#     # form_class = UserCreationForm
#     form_class = RegisterForm
#     template_name = 'accounts/signup.html'
#     success_url = 'login'
#
#     def get(self, request):
#         form = RegisterForm()
#         return render(request, 'accounts/signup.html', { 'form': form })
#
#     def form_valid(self, form):
#         """
#         This method is called when valid form data has been POSTed.
#         It should return an HttpResponse.
#         """
#         return super().form_valid(form)

class SignUpView(generic.CreateView):
    # form_class = UserCreationForm
    form_class = RegisterForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, { 'form': form })

class RegisterView(View):
    form_class = CustomUserCreationForm
    initial = {
        'form_name': 'Register Form'
    }
    template_name = 'accounts/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            messages.success(request, 'Account created successfully')
            # return HttpResponseRedirect('/login/')
            return redirect('login')

        return render(request, self.template_name, {'form': form})

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