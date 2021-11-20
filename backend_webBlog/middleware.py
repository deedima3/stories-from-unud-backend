import random

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.http import HttpResponse

class ApiAuthentication:
    def __init__(self, get_response):
        self.URLreqToken = [
            '/api/blog-post/',
            '/api/blog-post/one-item/',
            '/api/search/',
            '/api/create/article/',
        ]
        self.get_response = get_response

    def __call__(self, request):
        print(request.path)
        response = self.get_response(request)
        if (request.path in self.URLreqToken):
            if ('token' in request.headers):
                token = request.headers['Token']
                result = authenticate(username='EndPointAccess', password=token)
                if (result is not None):
                    pass
                else:
                    return Response(status=status.HTTP_403_FORBIDDEN)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
            return response
        elif (request.path == '/api/login/'):
            if ('usernamePOST' in request.POST and 'passwordPOST' in request.POST):
                result = authenticate(
                    username=request.POST['usernamePOST'],
                    password=request.POST['passwordPOST'],
                )
                if (result is not None):
                    sessionPart = SessionStore()
                    sessionPart['last_login'] = random.randint(1000000, 9999999)
                    sessionPart.create()
                    print(sessionPart.session_key)
                return response
        elif (request.path == '/api/adminValidator/'):
            if ('sessionID' in request.COOKIES):
                try:
                    getSession = Session.objects.get(pk=request.COOKIES['sessionID'])
                    return response
                except:
                    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

