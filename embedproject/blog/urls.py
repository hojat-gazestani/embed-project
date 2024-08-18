from django.urls import path, include
from embedproject.blog.apis.products import ProductApi

from .apis.post import PostApi, PostDetailApi
from .apis.subscription import SubscribeApi, SubscribeDetailApi

app_name = "blog"
urlpatterns = [
    path("products/", ProductApi.as_view(), name="products"),
    path("subscribe/", SubscribeApi.as_view(), name="subscribe"),
    path(
        "subscribe/<str:email>", SubscribeDetailApi.as_view(), name="subscribe_detail"
    ),
    path("post/", PostApi.as_view(), name="post"),
    path("post/<slug:slug>", PostDetailApi.as_view(), name="post_detail"),
]
