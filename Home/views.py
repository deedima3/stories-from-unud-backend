from django.urls import path, include
from django.contrib.auth.models import User
from DATABASE.serializers import BlogSerializers, BlogMainDatabase
from rest_framework import routers, serializers, viewsets

# Create your views here.
class HomeViewSet(viewsets.ModelViewSet):
    queryset = BlogMainDatabase.objects.all()
    serializer_class = BlogSerializers
    http_method_names = ['get']