from django.core.management.base import BaseCommand
from movie_api.models import Movie, Genre
from django.conf import settings
import json


class Command(BaseCommand):
    help = 'Populates the database from json file'

    def handle(self, *args, **kwargs):
        try:

            json_file = f'{settings.BASE_DIR}/imdb.json'

            with open(json_file) as file:
                movies_data = file.read()
                movies_list = json.loads(movies_data)
                single_movie = {}
                for movie_obj in movies_list:
                    single_movie['popularity'] = movie_obj.get('99popularity')
                    single_movie['director'] = movie_obj.get('director')
                    single_movie['imdb_score'] = movie_obj.get('imdb_score')
                    single_movie['name'] = movie_obj.get('name')

                    movie, created = Movie.objects.get_or_create(**single_movie)
                    genres = movie_obj.get('genre')

                    for genre in genres:
                        name = genre.strip()
                        genre, created = Genre.objects.get_or_create(name=name)
                        movie.genre.add(genre)
                    movie.save()

                self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
                return

        except IOError as e:
            self.stdout.write(self.style.ERROR(f'File not found. {e}'))
            return