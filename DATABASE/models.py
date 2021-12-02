from django.db import models

# Create your models here.
class BlogMainDatabase(models.Model):
    HashNumber = models.IntegerField(default=9999, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    imageUrl = models.CharField(max_length=255, blank=True, null=True)
    article = models.TextField()
    dateTimeCreated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    author = models.CharField(max_length=150)
    visitor = models.IntegerField(default=0)
    acceptByAdmin = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.title)

class queueArticle(models.Model):
    HashNumber = models.IntegerField(default=9999, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    imageUrl = models.CharField(max_length=255, blank=True, null=True)
    article = models.TextField()
    dateTimeCreated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    author = models.CharField(max_length=150)
    visitor = models.IntegerField(default=0)
    acceptByAdmin = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.title)

class comments(models.Model):
        name = models.CharField(max_length=100)
        comment = models.TextField()
        email = models.EmailField()
        article = models.ForeignKey(BlogMainDatabase, on_delete=models.CASCADE())

    def __str__(self):
        return "{}. {}|{}".format(self.id, self.name, self.article)