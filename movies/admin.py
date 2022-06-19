from django.contrib import admin

from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'year']
    search_fields = ['name']
    list_filter = ['year']
    filter_horizontal = ['actors']