from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from smart_sentiment import views

urlpatterns = [
    path('smart/', views.SmartSentiment.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
