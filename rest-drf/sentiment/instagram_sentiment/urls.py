from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from instagram_sentiment import views

urlpatterns = [
    path('instagram/', views.InstagramSentiment.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
