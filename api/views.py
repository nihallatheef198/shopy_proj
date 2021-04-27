from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from .serializer import products_serializer


# Create your views here.

@api_view(['GET'])
def get_routes(request):
    return Response('hello')

@api_view(['GET'])
def get_products(request):
    products = models.Products.objects.all()
    serializer = products_serializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product(request, pk):
    product = models.Products.objects.get(_id=pk)
    serializer = products_serializer(product, many=False)
    return Response(serializer.data)
