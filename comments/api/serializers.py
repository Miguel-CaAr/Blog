from rest_framework import serializers
from ..models import Comments
from users.api.serializers import UserSerializer


class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'content', 'created_at', 'user', 'post']

    def to_representation(self, instance):
        from posts.api.serializers import PostSerializer # Importacion diferida
        representation = super().to_representation(instance)
        representation['post'] = PostSerializer(instance.post).data['title']
        representation['user'] = UserSerializer(instance.user).data['username']
        return representation

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
