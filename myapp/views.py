from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post
from django.shortcuts import render
from rest_framework import generics


# Create your views here.

class PostViewSet(ModelViewSet):
    queryset=Post.objects.all()
    serializer_class = PostSerializer

class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

