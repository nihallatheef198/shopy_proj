from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('products/', views.get_products),
    path('products/<str:pk>', views.get_product),
    path('user/', views.get_user),
    path('user/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
