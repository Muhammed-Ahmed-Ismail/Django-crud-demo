from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies.models import Movie
from .serializers import MovieSerializer, CUMovieSerializer


@api_view(['GET'])
def get_all_movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_one_movie(request, movie_id):
    response = {'data': {}, 'status': status.HTTP_204_NO_CONTENT}
    try:
        movie = Movie.objects.get(id=movie_id)
        serializer = MovieSerializer(movie, many=False)
        response['data'] = serializer.data
        response['status'] = status.HTTP_200_OK
    except ObjectDoesNotExist:
        response['data'] = {'no content'}
        response['status'] = status.HTTP_204_NO_CONTENT
    except:
        response['data'] = {'internal server error'}
        response['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        return Response(**response)


@api_view(['POST'])
def post_movie(request):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        serializer = CUMovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['data'] = serializer.data
            response['status'] = status.HTTP_200_OK
        else:
            response['data'] = serializer.errors
    except:
        response['data'] = {'server error'}
        response['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        return Response(**response)


@api_view(['PUT', 'PATCH'])
def update_movie(request, movie_id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        movie_instance = Movie.objects.get(id=movie_id)

        if request.method == 'PUT':
            serializer = CUMovieSerializer(instance=movie_instance, data=request.data)
        else:  # PATCH
            serializer = CUMovieSerializer(instance=movie_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            response['data'] = serializer.data
            response['status'] = status.HTTP_200_OK
        else:
            response['data'] = serializer.errors
    except:
        response['data'] = {'bad request'}
        response['status'] = status.HTTP_400_BAD_REQUEST
    finally:
        return Response(**response)


@api_view(['DELETE'])
def delete_movie(request, movie_id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        Movie.objects.get(id=movie_id).delete()
        response['data'] = {'deleted'}
        response['status'] = status.HTTP_204_NO_CONTENT
    except ObjectDoesNotExist:
        response['data'] = {'not found'}
        response['status'] = status.HTTP_404_NOT_FOUND
    finally:
        return Response(**response)
