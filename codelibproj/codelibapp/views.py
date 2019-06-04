from django.shortcuts import render
from .models import ResourceType, Website, Meetup, Developer, Book, Blog

# Create your views here.
def index(request):
    return render(request, 'codelibapp/index.html')

def getResourceTypes(request):
    resource_types_list = ResourceType.objects.all()
    return render(request, 'codelibapp/resource_types.html', {'resource_types_list' : resource_types_list})

def getBooks(request):
    books_list = Book.objects.all()
    return render(request, 'codelibapp/book_list.html', {'books_list' : books_list})

def getBlogs(request):
    blogs_list = Blog.objects.all()
    return render(request, 'codelibapp/blog_list.html', {'blogs_list' : blogs_list})

def getWebsites(request):
    websites_list = Website.objects.all()
    return render(request, 'codelibapp/website_list', {'websites_list' : websites_list})

def getMeetups(request):
    meetups_list = Meetup.objects.all()
    return render(request, 'codelibapp/meetups_list', {'meetups_list' : meetups_list})

def getDevelopers(request):
    developers_list = Developer.objects.all()
    return render(request, 'codelibapp/developers_list', {'developers_list' : developers_list})
