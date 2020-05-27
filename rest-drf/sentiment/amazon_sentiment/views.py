from django.shortcuts import render

from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
from amazon_sentiment.amazon_scraping import amazon_comment_extracion, amzaon_reviews_sentiment

from amazon_sentiment.models import Product
from amazon_sentiment.serializer import ProductSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AmazonSentiment(APIView):
    def post(self, request, format = None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            link = serializer.data['link']
            result = amazon_comment_extracion(link)
            result = amzaon_reviews_sentiment(result)
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
