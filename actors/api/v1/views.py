from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response

from actors.api.v1.permissions import CheckDevGroup
from actors.models import Actor
from actors.api.v1.serializers import ActorSerializer, GetActorsSerializer


class GetAllActors(ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = GetActorsSerializer


@api_view(['GET'])
def get_one_actor(request, actor_id):
    response = {'data': {}, 'status': status.HTTP_404_NOT_FOUND}
    try:
        actor = Actor.objects.get(id=actor_id)
        serializer = GetActorsSerializer(actor, many=False)
        response['data'] = serializer.data
        response['status'] = status.HTTP_200_OK
    except ObjectDoesNotExist:
        response['data'] = {'not found'}
        response['status'] = status.HTTP_204_NO_CONTENT
    except:
        response['data'] = {'server error'}
        response['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        return Response(**response)


@permission_classes([CheckDevGroup])
@api_view(['POST'])
def post_actor(request):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        serializer = ActorSerializer(data=request.data)
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


@permission_classes([CheckDevGroup])
@api_view(['PUT', 'PATCH'])
def update_actor(request, actor_id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        movie_instance = Actor.objects.get(id=actor_id)

        if request.method == 'PUT':
            serializer = ActorSerializer(instance=movie_instance, data=request.data)
        else:  # PATCH
            serializer = ActorSerializer(instance=movie_instance, data=request.data, partial=True)

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


@permission_classes([CheckDevGroup])
@api_view(['DELETE'])
def delete_actor(request, actor_id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        Actor.objects.get(id=actor_id).delete()
        response['data'] = {'deleted'}
        response['status'] = status.HTTP_204_NO_CONTENT
    except ObjectDoesNotExist:
        response['data'] = {'not found'}
        response['status'] = status.HTTP_404_NOT_FOUND
    finally:
        return Response(**response)
