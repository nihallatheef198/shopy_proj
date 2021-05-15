from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import  IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from api.serializer import user_serializer, user_serializer_token
from django.contrib.auth.models import User

from django.http import JsonResponse
from django.contrib.auth.hashers import make_password


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = request.user
    serializer = user_serializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users(request):
    user = User.objects.all()
    serializer = user_serializer(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def signup(request):
            try:
                data = request.data
                user = User.objects.create(
                    first_name=data['name'],
                    username=data['email'],
                    email=data['email'],
                    password=make_password(data['password'])
                )
                serializer = user_serializer_token(user, many=False)
                return Response(serializer.data)
            except Exception as e:
                print(str(e))
                return JsonResponse({'error':'user name already taken :('}, status=400)


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = user_serializer_token(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer