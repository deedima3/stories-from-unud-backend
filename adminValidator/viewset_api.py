import json
import random

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from DATABASE.models import BlogMainDatabase, queueArticle
from DATABASE.serializers import queueArticleSerialize


class antrianArticle:
    def __init__(self, datas):
        self.datas = datas
        self.dataQueue = []
        self.front = None
        self.rear = None

    def convertToQueue(self):
        for data in self.datas:
            self.enqueue(data)
        try:
            self.front = self.dataQueue[0]
            self.rear = self.dataQueue[-1]
        except:
            self.front = -1
            self.rear = -1
        return self.getAllQueue()

    def first(self):
        print(self.front)
        return self.front

    def last(self):
        print(self.rear)
        return self.rear

    def enqueue(self, data):
        self.dataQueue.append(data)

    def dequeue(self):
        return None# Not Implemented

    def getAllQueue(self):
        return self.dataQueue

# Create your views here.

class ApiBlogValidator(ListAPIView):
    queryset = antrianArticle(datas=queueArticle.objects.all()).convertToQueue()
    serializer_class = queueArticleSerialize
    pagination_class = PageNumberPagination

@api_view(['GET'])
def adminValidatorViewSet(request):
    dataResponse = {
        'status': 'OK'
    }
    queueKu = antrianArticle(datas=queueArticle.objects.all()).convertToQueue()
    dataSerializer = queueArticleSerialize(queueKu, many=True)
    return Response(dataSerializer.data)

@api_view(['POST'])
def login(request):
    bodyRequest = json.loads(request.body.decode('utf-8'))
    if ('usernameGET' in bodyRequest and 'passwordGET' in bodyRequest):
        result = authenticate(
            username=bodyRequest['usernameGET'],
            password=bodyRequest['passwordGET'],
        )
        if (result is not None):
            sessionPart = SessionStore()
            sessionPart['last_login'] = random.randint(1000000, 9999999)
            sessionPart.create()
            print(sessionPart.session_key)
            return Response({"success": "login success"}, headers={'sessionID': str(sessionPart.session_key)}, status=status.HTTP_200_OK, content_type='application/json')
        else:
            try:
                User.objects.get(username=bodyRequest['usernameGET'])
                return Response({"fail": "Wrong Password"}, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"fail": "both"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
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
    bodyRequest = json.loads(request.body.decode('utf-8'))
    if ('HashNumber' in bodyRequest):
        try:
            data = queueArticle.objects.get(HashNumber=int(bodyRequest['HashNumber']))
            BlogMainDatabase.objects.create(
                HashNumber=data.HashNumber,
                title=data.title,
                article=data.article,
                imageUrl=data.imageUrl,
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