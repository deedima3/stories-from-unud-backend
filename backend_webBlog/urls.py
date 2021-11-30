from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from PostBlog.viewset_api import PostBlogSetView, PostBlogOneItem, SearchArticle
from CreateNewPost.viewset_api import CreateNewSetView
from adminValidator.viewset_api import adminValidatorViewSet, login, logout, acceptArticle
from CreateNewPost.viewset_api import visitor

urlpatterns = [
    path('api/visitor-increment', visitor , name='Visitor Increment')
    path('api/blog-post/', PostBlogSetView, name='Page Blog Post'),               # GET with token Ba72o5PX4vIH
    path('api/blog-post/one-item/', PostBlogOneItem, name='Blog Dynamic Route'),  # POST with token Ba72o5PX4vIH

    path('api/search/', SearchArticle, name='Search Article'),                    # POST with token Ba72o5PX4vIH

    path('api/create/article/', CreateNewSetView, name='Page Create New Post'),   # POST with token Ba72o5PX4vIH

    path('api/adminValidator/', adminValidatorViewSet, name='Admin Validator Content'),   # GET or POST with token Ba72o5PX4vIH
    path('api/login/', login, name='Login'),
    path('api/logout/', logout, name='Logout'),
    path('api/acceptArticle/', acceptArticle, name='AcceptArticleByAdmin'),

    path('admin/', admin.site.urls),  # Admin Panel
]

urlpatterns = format_suffix_patterns(urlpatterns)
