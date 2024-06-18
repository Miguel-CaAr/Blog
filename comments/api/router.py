from rest_framework.routers import DefaultRouter
from .views import CommentsViewSet

router_comments = DefaultRouter()

router_comments.register(
    prefix='comments', basename='comments', viewset=CommentsViewSet)
