
"""
Database models for the portfolio content management system.

This module manages dynamic website content such as blog posts.
"""

from django.db import models


class BlogPost(models.Model):
    """
    Represent a bilingual blog post.

    Supports English and Japanese content with
    draft and published status.
    """

    class Status(models.TextChoices):
        """Available publishing states."""

        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    # English and Japanese titles
    title_en = models.CharField(max_length=200)
    title_ja = models.CharField(
        max_length=200,
        blank=True
    )

    # Unique URL identifier
    slug = models.SlugField(
        max_length=220,
        unique=True
    )

    # Short descriptions
    summary_en = models.TextField(blank=True)
    summary_ja = models.TextField(blank=True)

    # Main blog content
    body_en = models.TextField()
    body_ja = models.TextField(blank=True)
    
    # Blog cover image (optional)
    cover_image = models.ImageField(
        upload_to="blog/covers/",
        blank=True
    )


    # Publishing status
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT
    )

    # Automatic timestamps
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        """Define default blog ordering."""

        ordering = ["-created_at"]

    def __str__(self):
        """Return the English blog title."""
        return self.title_en