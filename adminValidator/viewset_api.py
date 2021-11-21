from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from DATABASE.models import BlogMainDatabase, queueArticle
from DATABASE.serializers import BlogSerializers, queueArticleSerialize
from django.contrib.auth import authenticate
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
import random

class antrianArticle:
    def __init__(self):
        self.dataQueue = queueArticle.objects.all()
        self.front = self.dataQueue.first()
        self.rear = self.dataQueue.last()

    def first(self):
        print(self.front)
        return self.front

    def last(self):
        print(self.rear)
        return self.rear

    def enqueue(self):
        return None# Not Implemented

    def dequeue(self):
        return None# Not Implemented

    def getAllQueue(self):
        return self.dataQueue

# Create your views here.
@api_view(['GET', 'POST'])
def adminValidatorViewSet(request):
    dataResponse = {
        'status': 'OK'
    }
    queueKu = antrianArticle()
    dataSerializer = queueArticleSerialize(queueKu.getAllQueue(), many=True)
    return Response(dataSerializer.data)

@api_view(['POST'])
def login(request):
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
            return HttpResponse(headers={'sessionID': str(sessionPart.session_key)}, status=status.HTTP_200_OK)
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout(request):
    if ('sessionID' in request.headers):
        try:
            Session.objects.get(pk=request.headers['sessionID']).delete()
            return HttpResponse(status=status.HTTP_200_OK)
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def acceptArticle(request):
    if ('HashNumber' in request.POST):
        try:
            data = queueArticle.objects.get(HashNumber=int(request.POST['HashNumber']))
            BlogMainDatabase.objects.create(
                HashNumber=data.HashNumber,
                title=data.title,
                article=data.article,
                author=data.author,
                visitor=data.visitor,
                acceptByAdmin=True
            )
            data.delete()
            return HttpResponse(status=status.HTTP_200_OK)
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)