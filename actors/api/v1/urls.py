from django.urls import path

from actors.api.v1.views import GetAllActors, get_one_actor, post_actor, update_actor, delete_actor

urlpatterns = [
    path('', GetAllActors.as_view(), name='get_all_gen'),
    path('<int:actor_id>', get_one_actor, name='details'),
    path('add', post_actor, name='add_one'),
    path('update/<int:actor_id>', update_actor, name='update'),
    path('delete/<int:actor_id>', delete_actor, name='delete'),
]
