from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from .serializer import products_serializer, user_serializer_token


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
def get_user(request):
    user = request.user
    serializer = user_serializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_product(request, pk):
    product = models.Products.objects.get(_id=pk)
    serializer = products_serializer(product, many=False)
    return Response(serializer.data)



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = user_serializer_token(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer