from django.shortcuts import render

# Create your views here.
# myapp/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializers import RegisterSerializer, LoginSerializer
from django.http import JsonResponse

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return JsonResponse({"message": "Login successful", "username": user.username})
