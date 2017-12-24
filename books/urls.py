from django.urls import path

from books.views import PublisherListView
from books.views import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView

urlpatterns = [
    path('publishers/', PublisherListView.as_view()),

    path('author/', AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('author/add/', AuthorCreateView.as_view(), name='author-add'),
    path('author/<int:pk>/edit/', AuthorUpdateView.as_view(), name='author-update'),
    path('author/<int:pk>/remove/', AuthorDeleteView.as_view(), name='author-delete'),
]