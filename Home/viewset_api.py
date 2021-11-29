from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from DATABASE.models import BlogMainDatabase
from DATABASE.serializers import BlogSerializers

# Create your views here.


@api_view(['GET'])
def BlogHomeViewSetView(request, format=None):
    if request.method == 'GET':
        blogs = BlogMainDatabase.objects.filter(acceptByAdmin=True)
        serializer = BlogSerializers(blogs, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)