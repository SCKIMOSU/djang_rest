from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication

from .models import Post
from .serializers import PostSerializer
from .permissions import AuthorCheckPermission


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (AuthorCheckPermission,)


class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PublicPostListAPIView(APIView):
    def get(self, request):
        qs = Post.objects.filter(is_public=True)
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)


public_post_list = PublicPostListAPIView.as_view()

# @api_view(['GET'])
# def public_post_list(request):
#    qs=Post.objects.filter(is_public=True)
#    serializer=PostSerializer(qs, many=True)
#    return Response(serializer.data)
