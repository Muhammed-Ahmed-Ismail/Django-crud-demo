from rest_framework import serializers
from movies.models import Movie

from actors.api.v1.serializers import ActorSerializer
from director.api.v1.serializers import DirectorSerializer


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    director = DirectorSerializer(many=False)

    class Meta:
        model = Movie
        fields = ['movie_name', 'production_year', 'director', 'actors', ]


class CUMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
