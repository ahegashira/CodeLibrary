from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getresourcetypes/', views.getResourceTypes, name='types'),
    path('getbooks/', views.getBooks, name='books'),
    path('getBookDetails/<int:id>', views.getBookDetails, name='book_detail'),
    path('newBook/', views.newBook, name = 'newbook'),
    path('getblogs/', views.getBlogs, name='blogs'),
    path('getBlogDetails/<int:id>', views.getBlogDetails, name='blog_detail'),
    path('newBlog/', views.newBlog, name = 'newblog'),
    path('getwebsites/', views.getWebsites, name='websites'),
    path('getWebsiteDetails/<int:id>', views.getWebsiteDetails, name='website_detail'),
    path('newWebsite/', views.newWebsite, name = 'newwebsite'),
    path('getmeetups/', views.getMeetups, name='meetups'),
    path('getMeetupDetails/<int:id>', views.getMeetupDetails, name='meetup_detail'),
    path('newMeetup/', views.newMeetup, name = 'newmeetup'),
    path('getdevelopers/', views.getDevelopers, name='developers'),
    path('getDeveloperDetails/<int:id>', views.getDeveloperDetails, name='developer_detail'),
    path('newDeveloper/', views.newDeveloper, name = 'newdeveloper'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]