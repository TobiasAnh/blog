from django.urls import path
from blog.views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

""" 
This script is part of the pattern:
URL > views > template 

Here url patterns are stored for the entire webpage including parameters ...
1) path (url address as a string, some dynamics allowed using <> ), 
2) view function (generating the html), 
3) name (for referencing) 

https://docs.djangoproject.com/en/4.1/ref/urls/

"""
urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("", BlogListView.as_view(), name="home"),
]
