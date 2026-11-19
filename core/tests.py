"""Regression tests for public pages and contact submissions."""
from django.test import TestCase
from django.urls import reverse
from .models import ContactMessage, Project


class PortfolioTests(TestCase):
    """Check homepage rendering, project visibility, and form handling."""

    def setUp(self):
        """Create a sample published project."""
        self.project = Project.objects.create(
            title="Sample Toolkit", slug="sample-toolkit", category="support",
            summary="Sample summary", description="Sample description",
            technologies="Python, Windows",
        )

    def test_homepage_loads_with_project(self):
        """The homepage lists published projects."""
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Toolkit")

    def test_project_detail_page(self):
        """Published case-study pages are reachable."""
        response = self.client.get(self.project.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample description")

    def test_hidden_project_not_public(self):
        """Unpublished projects return HTTP 404."""
        self.project.is_published = False
        self.project.save()
        self.assertEqual(self.client.get(self.project.get_absolute_url()).status_code, 404)

    def test_contact_form_saves(self):
        """Valid contact submissions are stored in the database."""
        response = self.client.post(reverse("core:home"), {
            "name": "Visitor", "email": "visitor@example.com", "message": "Hello!", "website": "",
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_honeypot_rejects_spam(self):
        """Bot-like submissions are not stored."""
        response = self.client.post(reverse("core:home"), {
            "name": "Bot", "email": "bot@example.com", "message": "Spam", "website": "https://spam.example",
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)
