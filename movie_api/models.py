from django.db import models
from movie_api.validator import validate_popularity,validate_imdb_score

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200,db_index=True)

    def __str__(self):
        return self.name

class Movie(models.Model):

    popularity = models.FloatField(validators=[validate_popularity])
    director = models.CharField(max_length = 200)
    imdb_score = models.FloatField(validators=[validate_imdb_score])
    name = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name
