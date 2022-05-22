from django import forms
from Blogs.models import Blog,BlogCategory,Events
class BlogCategoryForm(forms.ModelForm):
    class Meta():
        model = BlogCategory
        fields = ('Category_Id','Category_Name')

        widgets = {
            'Category_Id': forms.TextInput(attrs={'class': 'form-control'}),
            'Category_Name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BlogForm(forms.ModelForm):
    class Meta():
        model = Blog
        fields = ('title','description','photo','category','is_headline','is_popular')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=BlogCategory.objects.all(),attrs={'class': 'form-control'}),
            'is_headline': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_popular': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

class EventForm(forms.ModelForm):
    class Meta():
        model = Events
        fields = ('title','description','venue','date_of_event')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_event': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input', 'data-target':'#datetimepicker1'}),
        }