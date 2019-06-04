from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ResourceType(models.Model):
    resource_type = models.CharField(max_length = 255)
    resource_description = models.CharField(max_length = 255, null = True, blank = True)

    def __str__(self):
        return self.resource_type

    class Meta:
        db_table = 'resource'
        verbose_name_plural = 'resources'

class Book(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    resource_type = models.ForeignKey(ResourceType, on_delete = models.DO_NOTHING)
    book_title = models.CharField(max_length = 255)
    book_author = models.CharField(max_length = 255)
    book_publisher = models.CharField(max_length = 255)
    book_pages = models.IntegerField('Pages', null = True, blank = True)
    book_isbn10 = models.CharField(max_length = 10, null = True, blank = True)
    book_isbn13 = models.CharField(max_length = 14, null = True, blank = True)
    book_pub_date = models.DateField(null = True, blank = True)
    book_description = models.TextField()

    def __str__(self):
        return self.book_title

    class Meta:
        db_table = 'book'
        verbose_name_plural = 'books'

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    resource_type = models.ForeignKey(ResourceType, on_delete = models.DO_NOTHING)
    blog_title = models.CharField(max_length = 255)
    blog_author_first = models.CharField(max_length = 100, null = True, blank = True)
    blog_author_last = models.CharField(max_length = 100, null = True, blank = True)
    blog_url = models.CharField(max_length = 255)
    blog_postdate = models.DateField()
    blog_description = models.TextField()
    
    def __str__(self):
        return self.blog_title

    class Meta:
        db_table = 'blog'
        verbose_name_plural = 'blogs'

class Website(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    resource_type = models.ForeignKey(ResourceType, on_delete = models.DO_NOTHING)
    website_title = models.CharField(max_length = 255)
    website_url = models.URLField()
    website_description = models.TextField()

    def __str__(self):
        return self.website_title

    class Meta:
        db_table = 'website'
        verbose_name_plural = 'websites'

class Meetup(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    resource_type = models.ForeignKey(ResourceType, on_delete = models.DO_NOTHING)
    meetup_title = models.CharField(max_length = 255)
    meetup_url = models.URLField()
    meetup_city = models.CharField(max_length = 100)
    meetup_state = models.CharField(max_length = 2)
    meetup_description = models.TextField()

    def __str__(self):
        return self.meetup_title

    class Meta:
        db_table = 'meetup'
        verbose_name_plural = 'meetups'

class Developer(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    resource_type = models.ForeignKey(ResourceType, on_delete = models.DO_NOTHING)
    dev_first_name = models.CharField(max_length = 100)
    dev_last_name = models.CharField(max_length = 100)
    dev_twitter = models.CharField(max_length = 51)
    dev_specialty = models.TextField()

    def __str__(self):
        return self.dev_first_name

    class Meta:
        db_table = 'developer'
        verbose_name_plural = 'developers'