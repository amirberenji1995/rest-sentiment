from rest_framework import serializers
from smart_sentiment.models import Page

class PageSerializer(serializers.ModelSerializer):
    class Meta():
        model = Page
        fields = ['link']
