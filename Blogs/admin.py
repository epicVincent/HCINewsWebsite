from django.contrib import admin
from Blogs.models import Blog,BlogCategory,Events
# Register your models here.

admin.site.register(Blog)
admin.site.register(BlogCategory)
admin.site.register(Events)
