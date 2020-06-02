from rest_framework import serializers
from instagram_sentiment.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta():
        model = Post
        fields = ['link']
