"""
URL configuration for DocBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found
from DocBlog.views import index, index2
urlpatterns = [
    path('',index,name = 'index'),# index page
    path('index2/',index2,name = 'index2'),# index page
    path('admin/', admin.site.urls),# admin page
    path('irdof/', page_not_found, {'exception': Exception("Page non trouvée")}),# page not found
    path('blog/', include('blog.urls')),# blog page
]
