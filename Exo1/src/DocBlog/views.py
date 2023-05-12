from django.http import HttpResponse
from django.shortcuts import render
import datetime

def index(request):
    #return un bout de code HTML
    return HttpResponse("<h1>Hello, world. You're at the DocBlog index.</h1>")

def index2(request):
    #return un bout de code HTML
    return render(request, 'DocBlog/index.html', context={"message":"Here the message from the context","date": datetime.datetime.now()})