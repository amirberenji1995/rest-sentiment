from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_sentiment import views

urlpatterns = [
    path('sentiment/', views.Sentiment.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
