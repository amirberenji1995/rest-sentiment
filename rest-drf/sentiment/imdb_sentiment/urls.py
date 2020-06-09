from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from imdb_sentiment import views

urlpatterns = [
    path('imdb/', views.ImdbReviews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
