"""Database models for the projects gallery and visitor messages."""
from django.db import models
from django.urls import reverse


class Project(models.Model):
    """A portfolio project published through Django Admin."""

    class Category(models.TextChoices):
        SUPPORT = "support", "IT Support"
        PYTHON = "python", "Python & Automation"
        ERP = "erp", "ERP & SAP"
        WEB = "web", "Web Development"

    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, help_text="Used in the project page URL")
    category = models.CharField(max_length=20, choices=Category.choices)
    summary = models.CharField(max_length=270)
    description = models.TextField(help_text="Explain what the project does and why it matters")
    technologies = models.CharField(max_length=250, help_text="Comma-separated list, e.g. Python, Windows, CLI")
    key_features = models.TextField(blank=True, help_text="One feature per line")
    github_url = models.URLField(blank=True, help_text="Add your real repository URL when ready")
    demo_url = models.URLField(blank=True)
    featured = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
    sort_order = models.PositiveSmallIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "-updated_at"]

    def __str__(self):
        """Return the project title in admin lists."""
        return self.title

    def get_absolute_url(self):
        """Return the public detail page for the project."""
        return reverse("core:project_detail", kwargs={"slug": self.slug})

    @property
    def technology_list(self):
        """Return technology badges from the comma-separated field."""
        return [name.strip() for name in self.technologies.split(",") if name.strip()]

    @property
    def feature_list(self):
        """Return features from newline-separated text."""
        return [line.strip() for line in self.key_features.splitlines() if line.strip()]


class ContactMessage(models.Model):
    """Message submitted by a visitor via the portfolio contact form."""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        """Return a concise admin representation."""
        return f"{self.name} — {self.created_at:%Y-%m-%d}"
