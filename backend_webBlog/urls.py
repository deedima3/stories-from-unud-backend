from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from Home.viewset_api import BlogHomeViewSetView, BlogHomeOneItem
from PostBlog.viewset_api import BlogPostViewSetView

# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register('home', HomeViewSet)

urlpatterns = [
    path('api/home/', BlogHomeViewSetView),
    path('api/home/<int:pk>/', BlogHomeOneItem),
    path('api/newpost/', BlogPostViewSetView),
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
