import random
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.http import HttpResponse

class ApiPathFilter:
    def __init__(self, get_response):
        self.URLreqToken = [
            '/api/blog-post/',
            '/api/blog-post/one-item/',
            '/api/search/',
            '/api/create/article/',
            '/api/visitor-increment/',
        ]
        self.URLreqSessionID = [
            '/api/adminValidator/',
            '/api/acceptArticle/',
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
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
            else:
                return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
            return response
        elif (request.path in self.URLreqSessionID):
            if ('sessionID' in request.headers):
                try:
                    getSession = Session.objects.get(pk=request.headers['sessionID'])
                    pass
                except:
                    return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                return response
            else:
                return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return response

