import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from DATABASE.models import BlogMainDatabase, comments
from DATABASE.serializers import BlogSerializers, commentsSerializer
from CreateNewPost import ultilites
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView


def bubbleSort(listData):
    n = len(listData)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if (listData[j].visitor < listData[j + 1].visitor):
                listData[j], listData[j + 1] = listData[j + 1], listData[j]

class antrianComment:
    def __init__(self, hash):
        self.HashNumber = hash
        self.ForeignKey = BlogMainDatabase.objects.get(HashNumber=hash)
        self.dataQueue = list(comments.objects.filter(articleHash=hash).order_by('-id'))
        self.front = self.dataQueue[0]
        self.rear = self.dataQueue[-1]

    def first(self):
        print(self.front)
        return self.front

    def last(self):
        print(self.rear)
        return self.rear

    def enqueue(self, nameIn, commentIn, emailIn):
        comments.objects.create(
            name=nameIn,
            comment=commentIn,
            email=emailIn,
            articleHash=self.HashNumber,
            fkArticle=self.ForeignKey
        )
        self.dataQueue.insert(0, comments.objects.last())
        self.front = self.dataQueue[0]
        return self.dataQueue

    def dequeue(self):
        return None# Not Implemented

    def getAllQueue(self):
        return self.dataQueue

# Create your views here.

class ApiBlogListView(ListAPIView):
    queryset = BlogMainDatabase.objects.all()
    serializer_class = BlogSerializers
    pagination_class = PageNumberPagination

@api_view(['GET'])
def GETcomment(request):
    print(request.GET)
    if (str(request.method).lower() == 'get'):
        try:
            HashNumber = int(request.GET['HashNumber'])
            getAllComment = antrianComment(hash=HashNumber).getAllQueue()
            print(getAllComment)
            serializer = commentsSerializer(getAllComment, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def POSTCommnet(request):
    if (str(request.method).lower() == 'post'):
        try:
            bodyRequest = json.loads(request.body.decode('utf-8'))
            HashNumberBody = int(bodyRequest['HashNumber'])

            result = antrianComment(hash=HashNumberBody).enqueue(
                nameIn=bodyRequest['name'],
                commentIn=bodyRequest['comment'],
                emailIn=bodyRequest['email']
            )
            serializer = commentsSerializer(result, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['GET'])
def PostBlogSetView(request, format=None):
    if (str(request.method).lower() == 'get'):
        blogs = list(BlogMainDatabase.objects.filter(acceptByAdmin=True))
        if ('sorting' in request.GET):
            if (request.GET['sorting'] == 'yes'):
                bubbleSort(blogs)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = BlogSerializers(blogs, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def PostBlogOneItem(request, format=None):
    if (str(request.method).lower() == 'get'):
        try:
            try:
                HashNumber = int(request.GET['HashNumber'])
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            oneContent = BlogMainDatabase.objects.get(HashNumber=HashNumber)
            serializer = BlogSerializers(oneContent)
            return Response(serializer.data)
        except BlogMainDatabase.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def SearchArticle(request):
    if (str(request.method).lower() == 'get'):
        try:
            keyword = str(request.GET['keyword']).lower().replace('+', ' ')
            print(keyword)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data = ultilites.cekSearchLinearCollision(keyword=keyword)

        if (data):
            serializer = BlogSerializers(data)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def visitor(request):
    if (str(request.method).lower() == 'post'):
        try:
            try:
                bodyRequest = json.loads(request.body.decode('utf-8'))
                HashNumber = int(request.GET['HashNumber'])
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            Content = BlogMainDatabase.objects.get(HashNumber=HashNumber)
            Content.visitor += 1
            Content.save()
            serializer = BlogSerializers(Content)
            return Response(serializer.data)
        except BlogMainDatabase.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)