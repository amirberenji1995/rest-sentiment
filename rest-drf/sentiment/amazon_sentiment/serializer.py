from rest_framework import serializers
from amazon_sentiment.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = ['link']
