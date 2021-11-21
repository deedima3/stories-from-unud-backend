import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from DATABASE.models import BlogMainDatabase
from DATABASE.serializers import BlogSerializers
from CreateNewPost import ultilites

# Create your views here.

@api_view(['GET'])
def PostBlogSetView(request, format=None):
    if (str(request.method).lower() == 'get'):
        blogs = BlogMainDatabase.objects.filter(acceptByAdmin=True)
        serializer = BlogSerializers(blogs, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def PostBlogOneItem(request, format=None):
    if (str(request.method).lower() == 'get'):
        try:
            try:
                bodyRequest = json.loads(request.body.decode('utf-8'))
                HashNumber = int(bodyRequest['HashNumber'])
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
            bodyRequest = json.loads(request.body.decode('utf-8'))
            keyword = str(bodyRequest['keyword']).lower()
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