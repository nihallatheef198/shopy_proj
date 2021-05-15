from django.urls import path
from api.views import user_views as views

urlpatterns = [
    path('', views.get_user),
    path('all/', views.get_users),

    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup/', views.signup),
]
