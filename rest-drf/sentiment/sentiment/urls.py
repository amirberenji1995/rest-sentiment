
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('rest_sentiment.urls')),
    path('', include('amazon_sentiment.urls')),
    path('', include('instagram_sentiment.urls')),
    path('', include('imdb_sentiment.urls')),
    path('', include('smart_sentiment.urls')),
    ]
