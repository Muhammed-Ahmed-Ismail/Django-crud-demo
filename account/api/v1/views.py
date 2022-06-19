from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from account.api.v1.serializers import SignUpSerializer


@api_view(['POST'])
@permission_classes([])
def sign_up(request):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    serializer = SignUpSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        response['status'] = status.HTTP_200_OK
    else:
        response['data'] = serializer.errors
        response['status'] = status.HTTP_400_BAD_REQUEST

    return Response(**response)
