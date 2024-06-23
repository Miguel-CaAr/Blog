from rest_framework import serializers
from ..models import Post
from users.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'slug', 'miniature',
                  'created_at', 'published', 'user', 'category']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data['username']
        representation['category'] = CategorySerializer(
            instance.category).data['title']
        return representation

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
