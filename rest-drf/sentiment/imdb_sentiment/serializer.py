from rest_framework import serializers
from imdb_sentiment.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['link']
