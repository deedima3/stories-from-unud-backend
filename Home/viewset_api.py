from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from DATABASE.models import BlogMainDatabase
from DATABASE.serializers import BlogSerializers

# Create your views here.


@api_view(['GET'])
def BlogHomeViewSetView(request, format=None):
    if request.method == 'GET':
        blogs = BlogMainDatabase.objects.all()
        serializer = BlogSerializers(blogs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BlogSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def BlogHomeOneItem(request, pk, format=None):
    try:
        oneContent = BlogMainDatabase.objects.get(id=pk)
    except BlogMainDatabase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializers(oneContent)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        oneContent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)