from django.urls import path, include

urlpatterns = [
    path("blog/", include(("embedproject.blog.urls", "blog"))),
    path("users/", include(("embedproject.users.urls", "users"))),
    path("auth/", include(("embedproject.authentication.urls", "auth"))),
    # path('products/', ProductApi.as_view(), name='products'),
]
