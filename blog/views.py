from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .models import Post
from .serializers import PostListSerializer, UserRegistrationSerializer
from django.contrib.auth.models import User

class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostDetailView(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
