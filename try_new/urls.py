from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='try_new_home'),
    path('person/', views.list_person, name='list_person'),
    path('person/add/', views.add_person, name='add_person'),
    # url(r'^register/$', views.register, name='register'),
    # path('', views.BlogListView.as_view(), name='home'),
    # path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    # path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    # path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    # path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
]