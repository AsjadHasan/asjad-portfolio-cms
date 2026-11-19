"""Create initial project cards without overwriting later admin edits."""
from django.core.management.base import BaseCommand
from core.models import Project


EXAMPLE_PROJECTS = [
    {
        "slug": "windows-it-support-toolkit",
        "title": "Windows IT Support Toolkit",
        "category": Project.Category.SUPPORT,
        "summary": "A Python-based command-line toolkit for everyday Windows diagnostics and support tasks.",
        "description": "A practical IT support project built to explore Windows troubleshooting workflows, system information gathering, and command-line utilities. Add your actual implementation details and screenshots before sharing with recruiters.",
        "technologies": "Python, Windows, CLI, Troubleshooting",
        "key_features": "Display system information\nInspect memory and disk usage\nOrganize troubleshooting tasks in a menu-driven interface",
        "sort_order": 1,
    },
    {
        "slug": "python-system-admin-toolkit",
        "title": "Python System Administration Toolkit",
        "category": Project.Category.PYTHON,
        "summary": "A collection of Python utilities for system overview, disk monitoring, backups, and logs.",
        "description": "A Python system administration learning project combining routine desktop tasks into a single command-line toolkit. Update this case study with your verified output and codebase details.",
        "technologies": "Python, File Handling, ZIP Backups, Logging",
        "key_features": "View system overview\nMonitor disk usage\nCreate ZIP folder backups\nInspect recent log entries",
        "sort_order": 2,
    },
    {
        "slug": "active-directory-helpdesk-simulator",
        "title": "Active Directory Helpdesk Simulator",
        "category": Project.Category.SUPPORT,
        "summary": "A helpdesk-oriented simulation project for practicing identity and account support workflows.",
        "description": "A portfolio exercise focused on simulating common helpdesk processes. This is a learning simulator, not a claim of production Active Directory administration experience. Add the exact implemented functionality from your repository.",
        "technologies": "Python, OOP, Helpdesk, Simulation",
        "key_features": "Practice simulated support scenarios\nOrganize logic with Python classes\nTest helpdesk workflow behaviors",
        "sort_order": 3,
    },
]


class Command(BaseCommand):
    """Add initial project records only when they do not exist."""

    help = "Seed three editable portfolio projects"

    def handle(self, *args, **options):
        """Create projects idempotently and preserve later admin edits."""
        count = 0
        for entry in EXAMPLE_PROJECTS:
            data = entry.copy()
            slug = data.pop("slug")
            _, created = Project.objects.get_or_create(slug=slug, defaults=data)
            count += bool(created)
        self.stdout.write(self.style.SUCCESS(f"Created {count} new project(s). Existing projects were not changed."))
