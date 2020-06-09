from imdb_sentiment.models import Movie
from imdb_sentiment.serializer import MovieSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from imdb_sentiment.imdb_scraper import imdb_reviews


class ImdbReviews(APIView):
    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            link = serializer.data['link']
            result = imdb_reviews(link)
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
