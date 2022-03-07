
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from Hello import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='home'),
    path('shopping.html', views.shopping, name='home'),
    path('login.html', views.login, name='home'),
]
