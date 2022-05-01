from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from movie_api.models import Movie
from movie_api.serializers import MovieSerializer


# Create your views here.

class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    search_fields = ['name', 'director','popularity','imdb_score', 'genre__name']
    
    ordering_fields = ['popularity','imdb_score']

