from django.test import TestCase
from .models import ResourceType, Book, Blog, Website, Meetup, Developer
from django.urls import reverse
from django.contrib.auth.models import User 
import datetime
from .forms import  WebsiteForm, MeetupForm, DeveloperForm, BookForm, BlogForm

# Testing Models:
# Test ResourceType
class ResourceTypeTest(TestCase):

    def test_resourcestringOutput(self):
        resource=ResourceType(resource_type='New Type')
        self.assertEqual(str(resource), resource.resource_type)

    def test_resourcetypetablename(self):
        self.assertCountEqual(str(ResourceType._meta.db_table), 'resource')

# Test Book
class BookTest(TestCase):

    def setUp(self):
        self.type=ResourceType(resource_type='New Book Resource Type')
        self.book_detail=Book(book_title='New Title',resource_type=self.type)
    
    def test_string(self):
        self.assertEqual(str(self.book_detail),self.book_detail.book_title)

    def test_bookstringOutput(self):
        book=Book(book_title='New Book')
        self.assertEqual(str(book), book.book_title)

    def test_booktablename(self):
        self.assertCountEqual(str(Book._meta.db_table), 'book')

# Test Blog
class BLogTest(TestCase):

    def setUp(self):
        self.type=ResourceType(resource_type='New BLog Resource Type')
        self.blog_detail=Blog(blog_title='New Blog Title',resource_type=self.type)
    
    def test_string(self):
        self.assertEqual(str(self.blog_detail),self.blog_detail.blog_title)

    def test_blogstringOutput(self):
        blog=Blog(blog_title='New Blog')
        self.assertEqual(str(blog), blog.blog_title)

    def test_blogtablename(self):
        self.assertCountEqual(str(Blog._meta.db_table), 'blog')

# Test Website
class WebsiteTest(TestCase):

    def setUp(self):
        self.type=ResourceType(resource_type='New Website Resource Type')
        self.website_detail=Website(website_title='New Website Title',resource_type=self.type)
    
    def test_string(self):
        self.assertEqual(str(self.website_detail),self.website_detail.website_title)

    def test_websitestringOutput(self):
        website=Website(website_title='New Website')
        self.assertEqual(str(website), website.website_title)

    def test_websitetablename(self):
        self.assertCountEqual(str(Website._meta.db_table), 'website')

# Test Meetup
class MeetupTest(TestCase):

    def setUp(self):
        self.type=ResourceType(resource_type='New Meetup Resource Type')
        self.meetup_detail=Meetup(meetup_title='New Meetup Title',resource_type=self.type)
    
    def test_string(self):
        self.assertEqual(str(self.meetup_detail),self.meetup_detail.meetup_title)

    def test_meetupstringOutput(self):
        meetup=Meetup(meetup_title='New Meetup')
        self.assertEqual(str(meetup), meetup.meetup_title)

    def test_meetuptablename(self):
        self.assertCountEqual(str(Meetup._meta.db_table), 'meetup')

# Test Developer
class DeveloperTest(TestCase):

    def setUp(self):
        self.type=ResourceType(resource_type='New Developer Resource Type')
        self.developer_detail=Developer(dev_first_name='New Developer',resource_type=self.type)
    
    def test_string(self):
        self.assertEqual(str(self.developer_detail),self.developer_detail.dev_first_name)

    def test_developerstringOutput(self):
        developer=Developer(dev_first_name='New Developer')
        self.assertEqual(str(developer), developer.dev_first_name)

    def test_developertablename(self):
        self.assertCountEqual(str(Developer._meta.db_table), 'developer')


# Testing Views, Forms, Template:
# Test IWebsiteFormndex
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'codelibapp/index.html')

# Test getResourceTypes
class TestGetResource(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/codelibapp/types')
        self.assertEqual(response.status_code, 404)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('types'))
        self.assertEqual(response.status_code, 200)

    #Testing the template resource.html    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('types'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'codelibapp/resource_types.html')
 

# Test getBooks
class TestGetBooks(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/codelibapp/books')
        self.assertEqual(response.status_code, 404)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)

    #Testing the template resource.html    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'codelibapp/book_list.html')

#Test newBook form
class New_Book_Form_Test(TestCase):

    def setUp(self):
        self.user =User.objects.create(username='TestUser', password='P@ssw0rd1')
        self.type=ResourceType.objects.create(resource_type='type')

    def test_bookFormValid(self):
        data={
            'book_title': 'TestTitle',
            'resource_type' :  self.type,
            'user' : self.user,
            'book_author' : 'TestAuthor',
            'book_publisher' : 'TestPublisher' 
        }
        form = BookForm(data=data)
        self.assertTrue(form.is_valid) 
    
    def test_bookFormInvalid(self):
        data={
            'book_title': 'TestTitle',
            'resource_type' :  self.type,
            'user' : self.user,
            'book_author' : 'TestAuthor',
            'book_publisher' : 'TestPublisher' 
        }
        form = BookForm(data=data)
        self.assertFalse(form.is_valid()) 

# Test NewBook authentication
class New_Book_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='TestUser', password='P@ssw0rd1')
        self.type=ResourceType.objects.create(resource_type='TsetBook')
        self.book = Book.objects.create(resource_type=self.type, user=self.test_user, book_title='TestTitle', book_author='TestAuthor', book_publisher='TestPublisher', book_pages=250, book_description='New Test Book Authentication')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newbook'))
        self.assertRedirects(response, '/accounts/login/?next=/codelibapp/newBook/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='TestUser', password='P@ssw0rd1')
        response=self.client.get(reverse('newbook'))
        self.assertEqual(str(response.context['user']), 'TestUser')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'codelibapp/newbook.html')

# Test getBookDetails
class TestGetBookDetails(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/codelibapp/book_detail')
        self.assertEqual(response.status_code, 404) 

# Test getBlogs
class TestGetBlogs(TestCase):
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/codelibapp/blogs')
        self.assertEqual(response.status_code, 404)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)

    #Testing the template resource.html    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'codelibapp/blog_list.html')
        
# Test getBlogDetails
class TestGetBlogDetails(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/codelibapp/blog_detail')
        self.assertEqual(response.status_code, 404) 

# Test loginmessage
class TestLoginMessage(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/codelibapp/loginmessage')
        self.assertEqual(response.status_code, 301)
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('loginmessage'))
        self.assertEqual(response.status_code, 200)
    
    #Testing the template loginmessage.html
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('loginmessage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'codelibapp/loginmessage.html')

# Test logoutmessage
class TestLogoutMessage(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/codelibapp/logoutmessage')
        self.assertEqual(response.status_code, 301)
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('logoutmessage'))
        self.assertEqual(response.status_code, 200)

    #Testing the template logoutmessage.html
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('logoutmessage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'codelibapp/logoutmessage.html')






