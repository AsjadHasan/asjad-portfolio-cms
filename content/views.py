"""
Public views for the Portfolio CMS.

This module handles blog content displayed
on the public portfolio website.
"""

from django.shortcuts import render, get_object_or_404

from .models import BlogPost


def blog_list(request):
    """
    Display all published blog posts.

    Draft posts are excluded from public pages.
    Newest posts appear first.
    """

    posts = BlogPost.objects.filter(
        status=BlogPost.Status.PUBLISHED
    ).order_by("-created_at")

    context = {
        "posts": posts,
    }

    return render(
        request,
        "content/blog_list.html",
        context
    )
    

def blog_detail(request, slug):
    """
    Display the complete published blog article.

    Draft articles remain hidden from public visitors.
    """

    post = get_object_or_404(
        BlogPost,
        slug=slug,
        status=BlogPost.Status.PUBLISHED
    )

    return render(
        request,
        "content/blog_detail.html",
        {"post": post}
    )
