from django.db import models

# Create your models here.
class BlogMainDatabase(models.Model):
    HashNumber = models.IntegerField(default=9999, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    imageHeader = models.CharField(max_length=255, blank=True, null=True)
    article = models.TextField()
    dateCreated = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=150)

    def __str__(self):
        return "{}. {}".format(self.id, self.title)