from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getresourcetypes/', views.getResourceTypes, name='types'),
    path('getbooks/', views.getBooks, name='books'),
    path('getblogs/', views.getBlogs, name='blogs'),
    path('getwebsites/', views.getWebsites, name='websites'),
    path('getmeetups/', views.getMeetups, name='meetups'),
    path('getdevelopers/', views.getDevelopers, name='developers'),
]