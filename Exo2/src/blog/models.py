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
    
class Author(models.Model):
    firstname = models.CharField(max_length=35,blank=False)
    lastname = models.CharField(max_length=35,blank=False)
    wikipedia = models.URLField(blank=True,null=True)
    
    def __str__(self):
        return "{} {}".format(self.firstname,self.lastname)
    
class Book(models.Model):
    Aventure = 'AV'
    Thriller = 'TH'
    Romance = 'RO'
    Fantastique = 'FA'
    Horreur = 'HO'
    ScienceFiction = 'SF'
    Category = [
        (Aventure,'Aventure'),
        (Thriller,'Thriller'),
        (Romance,'Romance'),
        (Fantastique,'Fantastique'),
        (Horreur,'Horreur'),
        (ScienceFiction,'Science-Fiction'),
    ]
    
    
    title = models.CharField(max_length=35,blank=False)
    price = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    summary = models.TextField(blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=2,choices=Category,blank=True,null=True)
    stock = models.IntegerField(default=0)
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.title