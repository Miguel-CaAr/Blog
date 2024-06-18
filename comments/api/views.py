from rest_framework.viewsets import ModelViewSet
from ..models import Comments
from .serializers import CommentsSerializers
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrReadAndCreateOnly

class CommentsViewSet(ModelViewSet):
  permission_classes = [IsOwnerOrReadAndCreateOnly]
  serializer_class = CommentsSerializers
  queryset = Comments.objects.all()
  filter_backends = [OrderingFilter, DjangoFilterBackend]
  ordering = ['-created_at'] # Con el '-' se ordena del registro nuevo al antiguos
  filterset_fields = ['post']