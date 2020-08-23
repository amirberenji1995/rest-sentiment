
from django.contrib import admin
from django.urls import path, include

api_urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_sentiment.urls')),
    path('', include('amazon_sentiment.urls')),
    path('', include('instagram_sentiment.urls')),
    path('', include('imdb_sentiment.urls')),
    path('', include('smart_sentiment.urls')),
    path('api/v1/', include(api_urlpatterns)),
]
