from django.core.exceptions import ValidationError


def validate_popularity(value):
    if value < 0.0 or value > 100.0:
        raise ValidationError(('%(value)s must be in the range [0.0, 100.0]'), params={'value': value})


def validate_imdb_score(value):
    if value < 0.0 or value > 10.0:
        raise ValidationError(('%(value)s must be in the range [0.0, 100.0]'), params={'value': value})