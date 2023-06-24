from django.db import models

from users.models import *

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    banner = models.ImageField(upload_to='media/banners', blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    text = models.TextField()
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        if self.slug == None:
            self.slug = self.title.replace(' ', '-').lower()
            self.save()
        return self.title
    

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.profile.user.username
    

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    