"""View functions for the homepage, detail pages, and contact form."""
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ContactForm
from .models import Project


def home(request):
    """Render the homepage and process a validated contact submission."""
    contact_form = ContactForm(request.POST or None)
    if request.method == "POST" and contact_form.is_valid():
        contact_form.save()
        messages.success(request, "Thanks for reaching out! Your message has been saved.")
        return redirect(reverse("core:home") + "#contact")

    projects = Project.objects.filter(is_published=True)
    return render(
        request,
        "core/home.html",
        {
            "projects": projects,
            "contact_form": contact_form,
            "form_has_errors": request.method == "POST" and not contact_form.is_valid(),
        },
    )


def project_detail(request, slug):
    """Show a published project, or a 404 for hidden projects."""
    project = get_object_or_404(Project, slug=slug, is_published=True)
    return render(request, "core/project_detail.html", {"project": project})
