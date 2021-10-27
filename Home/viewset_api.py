from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from DATABASE.models import BlogMainDatabase
from DATABASE.serializers import BlogSerializers

# Create your views here.


@api_view(['GET'])
def BlogHomeViewSetView(request, format=None):
    if request.method == 'GET':
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