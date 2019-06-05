from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getresourcetypes/', views.getResourceTypes, name='types'),
    path('getbooks/', views.getBooks, name='books'),
    path('getBookDetails/<int:id>', views.getBookDetails, name='book_detail'),
    path('getblogs/', views.getBlogs, name='blogs'),
    path('getBlogDetails/<int:id>', views.getBlogDetails, name='blog_detail'),
    path('getwebsites/', views.getWebsites, name='websites'),
    path('getWebsiteDetails/<int:id>', views.getWebsiteDetails, name='website_detail'),
    path('getmeetups/', views.getMeetups, name='meetups'),
    path('getMeetupDetails/<int:id>', views.getMeetupDetails, name='meetup_detail'),
    path('getdevelopers/', views.getDevelopers, name='developers'),
    path('getDeveloperDetails/<int:id>', views.getDeveloperDetails, name='developer_detail'),
]