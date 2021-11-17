from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from DATABASE.models import BlogMainDatabase
from DATABASE.serializers import BlogSerializers
from CreateNewPost import ultilites
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.


@api_view(['GET'])
def PostBlogSetView(request, format=None):
    print(request.headers['Token'])
    if (request.method == 'GET'):
        if ('token' in request.headers):
            token = request.headers['Token']
            result = authenticate(username='EndPointAccess', password=token)
            if (result is not None):
                pass
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

        blogs = BlogMainDatabase.objects.filter(acceptByAdmin=True)
        serializer = BlogSerializers(blogs, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def PostBlogOneItem(request, format=None):
    if ('token' in request.GET):
        token = request.GET['token']
        if (token == 'Ba72o5PX4vIH'):
            pass
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

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
        return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
def SearchArticle(request):
    if (request.method == 'POST'):
        if ('token' in request.POST):
            token = request.POST['token']
            if (token == 'Ba72o5PX4vIH'):
                pass
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

        keyword = request.POST['keyword']
        data = ultilites.cekSearchLinearCollision(keyword=keyword)

        if (data):
            serializer = BlogSerializers(data)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    