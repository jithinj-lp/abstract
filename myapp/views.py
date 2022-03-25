from rest_framework.views import APIView, status
from . import serializers
from rest_framework.response import Response
from .models import *

class ProductView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'detail':'Product created'}, status=status.HTTP_201_CREATED)
        return Response(data={'detail':'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    