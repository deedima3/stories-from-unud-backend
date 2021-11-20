from django.contrib import admin

from DATABASE.models import BlogMainDatabase, queueArticle

# Register your models here.
admin.site.register(BlogMainDatabase)
admin.site.register(queueArticle)