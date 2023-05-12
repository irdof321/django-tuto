from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return un bout de code HTML
       return render(request, 'blog/index.html')
   
def article(request, numero_article):
    #return un bout de code HTML
    if numero_article not in ['1','2','3']:
        return render(request, 'blog/article-non-trouve.html')
    return render(request, 'blog/article{}.html'.format(numero_article))