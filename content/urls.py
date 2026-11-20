
"""
URL configuration for the Portfolio CMS.

Defines routes for public blog pages.
"""

from django.urls import path

from . import views


app_name = "content"

urlpatterns = [
    path("", views.blog_list, name="blog_list"),
    
    path(
        "<slug:slug>/",
        views.blog_detail,
        name="blog_detail"
    ),
]
