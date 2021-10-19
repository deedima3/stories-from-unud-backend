from django.db import models

# Create your models here.
class BlogMainDatabase(models.Model):
    HashNumber = models.IntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    imageHeader = models.CharField(max_length=255, blank=True, null=True)
    article = models.TextField()
    dateCreated = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=150)