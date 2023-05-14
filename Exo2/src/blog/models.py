from typing import Iterable, Optional
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

class BlogPost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateTimeField(blank=True,null=True)
    content = models.TextField()
    description = models.TextField(default="")
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.title