from django import forms
from .models import Website, Meetup, Developer, Book, Blog

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = '__all__'

class MeetupForm(forms.ModelForm):
    class Meta:
        model = Meetup
        fields = '__all__'

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'