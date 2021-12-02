from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from PostBlog.viewset_api import (
    PostBlogSetView,
    PostBlogOneItem,
    SearchArticle,
    visitor,
    ApiBlogListView
)
from CreateNewPost.viewset_api import CreateNewSetView
from adminValidator.viewset_api import (
    adminValidatorViewSet,
    login,
    logout,
    acceptArticle,
    ApiBlogValidator
)

urlpatterns = [
    path('api/visitor-increment/', visitor, name='Visitor Increment'),

    path('api/blog-post/one-item/', PostBlogOneItem, name='Blog Dynamic Route'),
    path('api/blog-post/list', ApiBlogListView.as_view(), name='Page Blog Post Pagination'),
    path('api/blog-post/', PostBlogSetView, name='Page Blog Post All'),

    path('api/search/', SearchArticle, name='Search Article'),

    path('api/create/article/', CreateNewSetView, name='Page Create New Post'),

    path('api/adminValidator/list', ApiBlogValidator.as_view(), name='Admin Validator Content Pagination'),
    path('api/adminValidator/', adminValidatorViewSet, name='Admin Validator Content All'),
    path('api/login/', login, name='Login'),
    path('api/logout/', logout, name='Logout'),
    path('api/acceptArticle/', acceptArticle, name='AcceptArticleByAdmin'),

    path('admin/', admin.site.urls),  # Admin Panel
]

urlpatterns = format_suffix_patterns(urlpatterns)
