from django.test import TestCase
from .models import ResourceType, Book, Blog, Website, Meetup, Developer
from django.urls import reverse
from django.contrib.auth.models import User
import datetime
""" from .forms import """

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
# Test Index
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

""" #newResource check the form
class New_ResourceForm_Test(TestCase):

def setUp(self):
self.test_user=User.objects.create_user(username='Mona', password='P@ssw0rd1')
self.resources_list = Resource.objects.create(resourcename='New Webpage', resourcetype='webpag', resourceurl='http://newwebpage.com', dateentered='2019-05-17', userid=self.test_user, resourcedescription='Good webpage to practice') """

# getBooks
class TestGetBook(TestCase):
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
# getBookDetails
# getBlogs
# getBlogDetails
# getWebsiteDetails
# getMeetups
# getMeetupDetails
# getDevelopers
# getDeveloperDetails