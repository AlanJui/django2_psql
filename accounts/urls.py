from django.conf.urls import url
from django.urls import path

from . import views
from try_new.views import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('register/', views.register, name='register'),
    path('register/', views.RegisterView.as_view(), name='register')
]