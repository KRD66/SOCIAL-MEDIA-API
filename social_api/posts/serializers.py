from rest_framework import serializers
from .models import Post, Comment, Profile
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
      likes_count =   serializers.IntegerField(source='likes.count', read_only=True)
class Meta:
        model = Post
        fields = '__all__'
 
        read_only_fields = ['author'] 
def create(self, validated_data):
      validated_data['author'] = self.context['request'].user
      return super().create(validated_data)
            
        

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'post']
    
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)    
            
        
class ProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    following_count = serializers.IntegerField(source='user.following.count', read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'followers_count', 'following_count']

