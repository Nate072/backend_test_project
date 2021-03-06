from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import render

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('firstName')
	serializer_class = UserSerializer
	permission_class = [permissions.IsAuthenticated]