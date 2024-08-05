from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews_movie')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'O mínimo é zero.'),
            MaxValueValidator(5, 'O máximo é cinco.'),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.movie)
