from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews_movie.aggregate(Avg('stars'))['stars__avg']

        return round(rate, 1) if rate else None

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('O resumo não pode conter mais que 500 caracteres.')
        return value

    def validate_release_date(self, value):
        if value.year < 1950:
            raise serializers.ValidationError('A data de lançamento do filme não pode ser anterior a 1950.')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):

    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'resume', 'rate']

    def get_rate(self, obj):
        rate = obj.reviews_movie.aggregate(Avg('stars'))['stars__avg']

        return round(rate, 1) if rate else None
