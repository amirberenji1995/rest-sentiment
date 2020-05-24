from rest_framework import serializers
from rest_sentiment.models import Sentence

class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = ['sen']
