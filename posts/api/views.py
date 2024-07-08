from rest_framework.viewsets import ModelViewSet
from ..models import Post
from .serializers import PostSerializer
from .permissions import IsAdminReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'
    # permission_classes = [IsAdminReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'title', 'category__title']
