from django.urls import path
from . import views

urlpatterns = [
    path('',views.perpro,name = "pprofile")
    
]