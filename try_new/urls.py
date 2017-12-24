from django.conf.urls import url
from django.urls import path

from . import views
from .views import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView
from .views import PersonListView, PersonDetailView, PersonCreateView, PersonUpdateView, PersonDeleteView

urlpatterns = [
    path('', PersonListView.as_view()),
    # path('home/', views.home, name='try_new_home'),

    path('person/', PersonListView.as_view(), name='person-list'),
    # path('person/<int:pk>/', views.show_detail, name='person-detail'),
    path('person/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
    path('person/add/', PersonCreateView.as_view(), name='person-create'),
    path('person/<int:pk>/edit/', PersonUpdateView.as_view(), name='person-update'),
    path('person/<int:pk>/remove/', PersonDeleteView.as_view(), name='person-delete'),

    path('author/', AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('author/add/', AuthorCreateView.as_view(), name='author-add'),
    path('author/<int:pk>/edit/', AuthorUpdateView.as_view(), name='author-update'),
    path('author/<int:pk>/remove/', AuthorDeleteView.as_view(), name='author-delete'),
]