from django.urls import path
from . import views

urlpatterns = [
    path('index.html',views.index,name='index'),
    path('contact.html',views.contact,name='contact'),
    path('knowmore.html',views.knowmore,name='knowmore'),
]