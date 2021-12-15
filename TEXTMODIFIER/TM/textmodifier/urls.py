from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="textmodifier"),
    path('index/', views.index, name='INDEX'),
    path('about.html/', views.about, name='ABOUTUS'),
    path('contact.html/', views.contact, name='CONTACTUS'),
    path('analyze.html/', views.analyze, name='ANALYZE'),
    path('error.html/', views.error, name='ERROR'),


]