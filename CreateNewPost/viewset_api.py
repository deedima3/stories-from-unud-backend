from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from DATABASE.serializers import BlogSerializers
from CreateNewPost.ultilites import hashfunction, cekLinearCollision
import requests

# Create your views here.
@api_view(['POST'])
def CreateNewSetView(request):
    if request.method == 'POST':
        if ('token' in request.POST):
            token = request.POST['token']
            if (token == 'Ba72o5PX4vIH'):
                pass
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

        print(request.data)

        kataKunci = request.data['title']
        keyHash = hashfunction(word=kataKunci)
        hasil = cekLinearCollision(keyNumber=keyHash)

        if (type(hasil) == int):
            keyHashFinal = hasil
        else:
            serializerError = BlogSerializers(data=request.data)
            serializerError.is_valid()
            return Response(serializerError.errors, status=status.HTTP_400_BAD_REQUEST) # Penyimpanan sudah penuh


        newData = {
            'HashNumber': keyHashFinal,
            'title': request.data['title'],
            'article': request.data['article'],
            'author': request.data['author']
        }

        serializer = BlogSerializers(data=newData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)