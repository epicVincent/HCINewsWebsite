from django.db import models

# Create your models here.
class Subscriber(models.Model):
    First_Name = models.CharField(max_length=200,blank=False,null=False)
    Last_name = models.CharField(max_length=200,blank=False,null=False)
    Email = models.EmailField()
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.First_Name + " "+self.Last_name
class Recents(models.Model):
    blog=models.ForeignKey('Blogs.Blog',on_delete=models.CASCADE,blank=False,null=False)
    subscriber= models.ForeignKey('subscriber',on_delete=models.CASCADE)
    first_viewed_at = models.DateTimeField(auto_now_add=True)
    last_viewed= models.DateTimeField(auto_now=True)

