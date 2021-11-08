from rest_framework import serializers

from DATABASE.models import BlogMainDatabase

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogMainDatabase
        fields = ['HashNumber', 'title', 'article', 'dateTimeCreated', 'author', 'visitor']