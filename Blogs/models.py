from django.db import models

# Create your models here.
import datetime

from django.urls import reverse


class BlogCategory(models.Model):
    Category_Id = models.CharField(max_length=200,blank=False,null=False)
    Category_Name = models.CharField(max_length=200,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.Category_Name

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = datetime.datetime.now()
        self.save()

    def get_absolute_url(self):
        return reverse('view_activitySlides')

    class Meta():
        ordering = ('-created_at',)
class Blog(models.Model):
    title = models.CharField(blank=False, null=False, max_length=200)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='blog_photos', null=True, blank=True)
    category=models.ForeignKey('BlogCategory',on_delete=models.RESTRICT,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_headline=models.BooleanField(default=False)
    is_popular=models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = datetime.datetime.now()
        self.save()

    def get_absolute_url(self):
        return reverse('view_activitySlides')

    class Meta():
        ordering = ('-created_at',)

class Events(models.Model):
    title = models.CharField(blank=False, null=False, max_length=200)
    description = models.TextField(blank=True, null=True)
    venue = models.CharField(max_length=200,blank=False,null=False)
    date_of_event = models.DateTimeField(default=datetime.datetime.today())
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True,null=True)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = datetime.datetime.now()
        self.save()

    class Meta():
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse('view_noticeEvents')