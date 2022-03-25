from unicodedata import name
from django.urls import path 
from . import views

urlpatterns = [ 
    path('create/product/', views.ProductView.as_view(), name='create-product'),
]