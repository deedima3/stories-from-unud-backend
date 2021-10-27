from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from DATABASE.models import BlogMainDatabase
from DATABASE.serializers import BlogSerializers
from CreateNewPost import ultilites

# Create your views here.


@api_view(['GET'])
def PostBlogSetView(request, format=None):
    if (request.method == 'GET'):
        if ('token' in request.GET):
            token = request.GET['token']
            if (token == 'Ba72o5PX4vIH'):
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
        searchResult = False
        hashResult = None
        # Logic Search
        # Logic Search
        # Logic Search
        # Logic Search

        if (searchResult):
            pass
        else:
            pass
    serializer = BlogSerializers(data=request.data)
    serializer.is_valid()
    return Response(serializer.errors, status=status.HTTP_501_NOT_IMPLEMENTED)