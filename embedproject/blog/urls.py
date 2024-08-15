from django.urls import path, include
from embedproject.blog.apis.products import ProductApi

urlpatterns = [
    path('products/', ProductApi.as_view(), name='products'),
]