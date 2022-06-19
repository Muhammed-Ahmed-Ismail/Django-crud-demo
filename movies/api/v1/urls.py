from movies.api.v1.views import get_all_movies, get_one_movie, post_movie, update_movie, delete_movie
from django.urls import path

urlpatterns = [
    path('', get_all_movies, name='get_all'),
    path('<int:movie_id>', get_one_movie, name='get_one'),
    path('add', post_movie, name='add_one'),
    path('update/<int:movie_id>', update_movie, name='update'),
    path('delete/<int:movie_id>', delete_movie, name='delete'),
]
