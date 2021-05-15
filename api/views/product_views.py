from rest_framework.decorators import api_view
from rest_framework.permissions import  IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from api.models import Products
from api.serializer import products_serializer



@api_view(['GET'])
def get_products(request):
    products = Products.objects.all()
    serializer = products_serializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product(request, pk):
    product = Products.objects.get(_id=pk)
    serializer = products_serializer(product, many=False)
    return Response(serializer.data)
