from DATABASE.models import BlogMainDatabase
from DATABASE.serializers import BlogSerializers
from CreateNewPost import ultilites
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class cekToken:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if ('token' in request.headers):
            token = request.headers['Token']
            result = authenticate(username='EndPointAccess', password=token)
            if (result is not None):
                pass
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

        response = self.get_response(request)
        return response