from django.urls import path
from .views import index, article

urlpatterns = [
    path('',index,name = 'blog-index'),# index page
    path('article-<str:numero_article>/',article,name = 'blog-article'),# index page
]
