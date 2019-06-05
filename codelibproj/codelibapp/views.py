from django.shortcuts import render, get_object_or_404
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

def getBookDetails(request, id):
    book_detail = get_object_or_404(Book, pk=id)
    context={
        'book_detail' : book_detail
    }
    return render(request, 'codelibapp/book_details.html', context=context)

def getBlogs(request):
    blogs_list = Blog.objects.all()
    return render(request, 'codelibapp/blog_list.html', {'blogs_list' : blogs_list})

def getBlogDetails(request, id):
    blog_detail = get_object_or_404(Blog, pk=id)
    context={
        'blog_detail' : blog_detail
    }
    return render(request, 'codelibapp/blog_details.html', context=context)

def getWebsites(request):
    websites_list = Website.objects.all()
    return render(request, 'codelibapp/website_list.html', {'websites_list' : websites_list})

def getWebsiteDetails(request, id):
    website_detail = get_object_or_404(Website, pk=id)
    context={
        'website_detail' : website_detail
    }
    return render(request, 'codelibapp/website_details.html', context=context)

def getMeetups(request):
    meetups_list = Meetup.objects.all()
    return render(request, 'codelibapp/meetup_list.html', {'meetups_list' : meetups_list})

def getMeetupDetails(request, id):
    meetup_detail = get_object_or_404(Meetup, pk=id)
    context={
        'meetup_detail' : meetup_detail
    }
    return render(request, 'codelibapp/meetup_details.html', context=context)

def getDevelopers(request):
    developers_list = Developer.objects.all()
    return render(request, 'codelibapp/developer_list.html', {'developers_list' : developers_list})

def getDeveloperDetails(request, id):
    developer_detail = get_object_or_404(Developer, pk=id)
    context={
        'developer_detail' : developer_detail
    }
    return render(request, 'codelibapp/developer_details.html', context=context)