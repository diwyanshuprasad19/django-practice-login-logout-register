# urls.py
from django.urls import path
from .views import UserLoginAPIView, UserLogoutAPIView, UserRegistrationAPIView

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='api_login'),
    path('logout/', UserLogoutAPIView.as_view(), name='api_logout'),
    path('register/', UserRegistrationAPIView.as_view(), name='api_register'),
]
