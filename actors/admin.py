from django.contrib import admin

from .models import Actor, Director
from movies.models import Movie


class MovieInline(admin.StackedInline):
    model = Movie
    extra = 1


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender', 'display_movies']
    search_fields = ('name')
    list_filter = ['gender']

    def display_movies(self, obj):
        return len(obj.movie_set.all())

    display_movies.short_description = 'Number of Movies'


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender']
    search_fields = ['name']
    list_filter = ['gender']
    inlines = [MovieInline]

    # def display_movies(self, obj):
    #     return len(obj.movie_set.all())
    #
    # display_movies.short_description='Number of Movies'
