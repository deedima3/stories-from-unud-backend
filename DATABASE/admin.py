from django.contrib import admin

from DATABASE.models import BlogMainDatabase, queueArticle, comments

# Register your models here.
admin.site.register(BlogMainDatabase)
admin.site.register(queueArticle)
admin.site.register(comments)