from rest_framework import status
from rest_framework_response import Response
from rest_framework_views import APIView
from rest_framework import serializers

from embedproject.api.paginations import LimitOffsetPagination

from embedproject.blog.models import Product
from embedproject.blog.services.products import create_product
from embedproject.blog.selectors.products import get_product

class ProductApi(APIView):

	class Pagination(LimitOsetPagination):
		default_limit = 15

	class InputSerializer(serializers.Serializer):
		name = serializers.CharField(max_length=255)

	class InputSerializer(serializers.ModelSerializer):

		class Meta:
			models = product
			fields = ("name", "created_at", "updated_at")

	def post(self, request):
		serializer = self.InputSerializer(data=request)
		serializer.is_valid(raise_exception=True)
		try:
			query = create_product(name=serializer.validated_data.get("name"))
		except Exception as ex:
			return Response(
				"Database Error {ex}",
				status=status.HTTP_400_BAD_REQUEST
				)
		return Response(self.OutPutSerializer(query, context={"request": request}).data)

	def get(set, request):
		query = get_products()
		return Response(self.OutPutSerializer(query, context={"request": request}, many=True).data)


