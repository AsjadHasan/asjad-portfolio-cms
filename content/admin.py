
"""
Django Admin configuration for the Portfolio CMS.

This module manages blog posts through the admin panel.
"""

from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """
    Configure the admin interface for blog management.

    Supports searching, filtering, editing,
    and publishing bilingual blog posts.
    """

    list_display = (
        "title_en",
        "status",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "title_en",
        "title_ja",
        "summary_en",
        "body_en",
    )

    prepopulated_fields = {
        "slug": ("title_en",),
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "English Content",
            {
                "fields": (
                    "title_en",
                    "summary_en",
                    "body_en",
                )
            },
        ),
        (
            "Japanese Content",
            {
                "fields": (
                    "title_ja",
                    "summary_ja",
                    "body_ja",
                )
            },
        ),
        
        (
            "Blog Cover Image",
            {
                "fields": (
                    "cover_image",
                )
            },
        ),

        (
            "Publishing Settings",
            {
                "fields": (
                    "slug",
                    "status",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
