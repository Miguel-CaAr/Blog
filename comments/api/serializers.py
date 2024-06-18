from rest_framework import serializers
from ..models import Comments
from posts.api.serializers import PostSerializer
from users.api.serializers import UserSerializer

class CommentsSerializers(serializers.ModelSerializer):
    post = PostSerializer()
    user = UserSerializer()
    class Meta:
        model = Comments
        fields = ['content', 'created_at', 'user', 'post']
