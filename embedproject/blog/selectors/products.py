from django.db.models import QuerySet
from embedproject.blog.models import Product


def get_products() -> QuerySet[Product]:
	return Product.object.all()
