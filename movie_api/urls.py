from django.urls import path
from movie_api.views import MovieList


urlpatterns = [
    path('movies', MovieList.as_view(), name = 'movies')
]
