from django.shortcuts import render

from urllib.parse import urlparse
from selenium import webdriver
import time
from smart_sentiment.smart_scraping import instagram_comments_scraper, imdb_reviews, amazon_comment_extracion, amzaon_reviews_sentiment, youtube_comments_scraper

from smart_sentiment.models import Page
from smart_sentiment.serializer import PageSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.throttling import UserRateThrottle


class SmartSentiment(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    throttle_classes = [UserRateThrottle]

    def post(self, request, format = None):
        serializer = PageSerializer(data=request.data)
        if serializer.is_valid():
            link = serializer.data['link']
            parse_object = urlparse(link)

            if parse_object.netloc == 'youtube.com' or parse_object.netloc == 'www.youtube.com':
                result = youtube_comments_scraper(link)
                return Response(result, status=status.HTTP_200_OK)
            elif parse_object.netloc == 'instagram.com' or parse_object.netloc == 'www.instagram.com':
                result = instagram_comments_scraper(link)
                return Response(result, status=status.HTTP_200_OK)
            elif parse_object.netloc == 'imdb.com' or parse_object.netloc == 'www.imdb.com':
                result = imdb_reviews(link)
                return Response(result, status=status.HTTP_200_OK)
            elif parse_object.netloc == 'amazon.com' or parse_object.netloc == 'www.amazon.com':
                result = amazon_comment_extracion(link)
                result = amzaon_reviews_sentiment(result)
                return Response(result, status=status.HTTP_200_OK)
            else:
                return Response(result, status=status.HTTP_404_NOT_FOUND)
