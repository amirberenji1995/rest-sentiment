from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from amazon_sentiment import views

urlpatterns = [
    path('amazon/', views.AmazonSentiment.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
