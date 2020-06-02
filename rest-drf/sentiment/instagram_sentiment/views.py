from django.shortcuts import render

from selenium import webdriver
import time
from instagram_sentiment.instagram_scraper import post_comments_scraper

from instagram_sentiment.models import Post
from instagram_sentiment.serializer import PostSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class InstagramSentiment(APIView):
    def post(self, request, format = None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            link = serializer.data['link']
            result = post_comments_scraper(link)
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
