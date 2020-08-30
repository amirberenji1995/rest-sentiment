from rest_sentiment.models import Sentence
from rest_sentiment.serializer import SentenceSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import permissions

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

class Sentiment(APIView):
    """
    Returns a JSON response, having float numbers as the indication of different sentiments.
    """
    def post(self, request, format=None):
        serializer = SentenceSerializer(data=request.data)
        if serializer.is_valid():
            sentence = serializer.data['sen']
            result = analyzer.polarity_scores(sentence)
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
