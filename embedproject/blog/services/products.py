from django.db.models import QuerySet
from embedproject.blog.models import Prod

def create_product(name: str) -> QuerySet[Product]:
	return Product.object.create(name=name)
