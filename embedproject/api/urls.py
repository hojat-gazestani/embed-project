from django.urls import path, include

urlpatterns = [
    path('blog/', include(('embedproject.blog.urls', 'blog'))),
    # path('products/', ProductApi.as_view(), name='products'),
]
