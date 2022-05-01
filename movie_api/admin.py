from django.contrib import admin
from movie_api.models import Movie,Genre

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    movie_display = ['name', 'director','popularity','imdb_score']
    
    search_fields = ['name', 'director','popularity','imdb_score']


class GenreAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Movie,MovieAdmin)
admin.site.register(Genre,GenreAdmin)