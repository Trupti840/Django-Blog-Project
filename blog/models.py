# blog/models.py

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name 

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='ForBloggers')
    author =models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    
    def __str__(self):
        return self.title +  ' | ' + str(self.author) + ' | ' + str(self.created_on)
    
    def get_absolute_url(self):
        return reverse('blog_detail', args=(str(self.id)))

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    def __str__(self):
        return self.body +  ' | ' + str(self.author) + ' | ' + str(self.created_on)
