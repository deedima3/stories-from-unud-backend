from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from DATABASE.serializers import BlogSerializers, queueArticleSerialize
from CreateNewPost.ultilites import hashfunction, cekLinearCollision
import requests

# Create your views here.
@api_view(['POST'])
def CreateNewSetView(request):
    if (str(request.method).lower() == 'post'):
        print(request.POST)

        kataKunci = str(request.POST['title']).lower()
        keyHash = hashfunction(word=kataKunci)
        hasil = cekLinearCollision(keyNumber=keyHash)

        if (type(hasil) == int):
            keyHashFinal = hasil
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        newData = {
            'HashNumber': keyHashFinal,
            'title': str(request.POST['title']).lower(),
            'imageUrl': request.POST['imageUpload'],
            'article': request.POST['article'],
            'author': request.POST['author']
        }

        serializer = queueArticleSerialize(data=newData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
