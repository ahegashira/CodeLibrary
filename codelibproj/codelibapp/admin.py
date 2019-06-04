from django.contrib import admin
from .models import ResourceType, Website, Meetup, Developer, Book, Blog

# Register your models here.
admin.site.register(ResourceType)
admin.site.register(Website)
admin.site.register(Meetup)
admin.site.register(Developer)
admin.site.register(Book)
admin.site.register(Blog)