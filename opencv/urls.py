from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
     path('opencvweb/', views.opencvweb, name= "opencvweb"),
     path('image/', views.image, name="image"),
     path('opencvweb/', views.image, name= "opencvweb"),
]