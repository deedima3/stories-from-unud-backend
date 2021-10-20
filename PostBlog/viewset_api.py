from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from DATABASE.models import BlogMainDatabase
from DATABASE.serializers import BlogSerializers
from PostBlog.ultilites import hashfunction, cekLinearCollision

# Create your views here.
@api_view(['GET', 'POST'])
def BlogPostViewSetView(request):
    if request.method == 'GET':
        blogs = BlogMainDatabase.objects.all()
        serializer = BlogSerializers(blogs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
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
            'imageHeader': request.data['imageHeader'],
            'article': request.data['article'],
            'dateCreated': request.data['dateCreated'],
            'author': request.data['author']
        }
        serializer = BlogSerializers(data=newData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)