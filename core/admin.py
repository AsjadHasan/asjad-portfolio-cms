"""Admin screens for projects and contact messages."""
from django.contrib import admin
from .models import ContactMessage, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Manage visible projects and ordering."""

    list_display = ("title", "category", "featured", "is_published", "sort_order", "updated_at")
    list_filter = ("category", "featured", "is_published")
    list_editable = ("featured", "is_published", "sort_order")
    search_fields = ("title", "description", "technologies")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Read contact messages in Django Admin."""

    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("name", "email", "message", "created_at")

    def has_add_permission(self, request):
        """Messages are created only from the public contact form."""
        return False
