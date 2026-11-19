# ASJAD / DEV — Premium Dark Portfolio (Django Starter)

A responsive, editable personal portfolio made with **HTML + CSS + vanilla JavaScript + Django 6.1**. Designed for an IT Support / Python / ERP career profile.

## 1) Requirements

- Windows 10/11 + PowerShell + VS Code
- Python 3.12–3.15, including **Python 3.14**
- Django 6.1.x (installed in a new virtual environment)

## 2) Quick start: Windows PowerShell

**Unzip** `asjad_portfolio_starter.zip` into your Django workspace. Then open the extracted `asjad_portfolio_starter` folder in VS Code.

In the integrated VS Code PowerShell terminal, run these commands one by one:

```powershell
# 1. Ensure you are in the folder containing manage.py
cd "E:\Code Bridge\batch3\django\asjad_portfolio_starter"

# 2. Create a project-specific virtual environment
python -m venv myenv

# 3. Activate it
.\myenv\Scripts\Activate.ps1

# 4. Install dependencies
python -m pip install -r requirements.txt

# 5. Generate project model migrations and database tables
python manage.py makemigrations core
python manage.py migrate

# 6. Create three editable project cards
python manage.py seed_projects

# 7. Start your local website
python manage.py runserver
```

The local site is **http://127.0.0.1:8000/**.

If PowerShell blocks virtual environment activation, run this **in the same terminal** and then retry activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\myenv\Scripts\Activate.ps1
```

**Important:** This folder is a new Django project. Do not merge its `config` or `core` directories into your existing `youtubeclone` project.

## 3) Open the admin dashboard

Stop the server with `Ctrl + C`, or open a second terminal where the environment is active:

```powershell
python manage.py createsuperuser
python manage.py runserver
```

Then open **http://127.0.0.1:8000/admin/**. Sign in and choose **Projects** to add, edit, reorder, publish, or unpublish items. Choose **Contact messages** to read submissions.

The `seed_projects` command creates records only if a slug does not already exist, so rerunning it will not overwrite your edits.

## 4) File structure

```text
asjad_portfolio_starter/
├── manage.py                         # Django command-line tool
├── requirements.txt                  # Dependency list
├── .gitignore
├── .env.example                      # Production configuration examples
├── config/
│   ├── settings.py                   # Django apps, database, static files
│   ├── urls.py                       # Main URL dispatcher
│   ├── wsgi.py
│   └── asgi.py
└── core/
    ├── admin.py                      # Project and message admin screens
    ├── apps.py
    ├── forms.py                      # Validated contact form + honeypot
    ├── models.py                     # Project and ContactMessage models
    ├── urls.py                       # Homepage / project detail routes
    ├── views.py                      # Database-driven page rendering
    ├── tests.py                      # 5 basic regression tests
    ├── migrations/
    │   └── __init__.py               # Generate 0001_initial.py locally
    ├── management/commands/
    │   └── seed_projects.py          # Initial example data
    ├── templates/core/
    │   ├── base.html                 # Shared navbar, footer, base HTML
    │   ├── home.html                 # Homepage sections + contact form
    │   └── project_detail.html       # Dynamic project case study page
    └── static/core/
        ├── css/styles.css            # Colors, layout, responsiveness
        ├── js/main.js                # Themes, filtering, reveals, menu
        └── img/favicon.svg           # Website favicon
```

## 5) How everything connects

**Browser → `config/urls.py` → `core/urls.py` → `core/views.py` → `core/models.py` (database) → `core/templates/core/home.html` (HTML)**

- **HTML/Django template:** Page layout and text, loops through project records.
- **CSS:** Color tokens, gradients, card layout, dark/light mode, breakpoints.
- **JavaScript:** Interactive menus, category filters, scroll reveal, saved theme.
- **Django model:** Defines fields stored in SQLite (the local development database).
- **Django Admin:** Lets you update projects without editing template files.

## 6) Make the portfolio yours

1. **Name, tagline and experience:** edit `core/templates/core/home.html` and `core/templates/core/base.html`.
2. **Colors:** edit CSS custom properties at the very top of `core/static/core/css/styles.css`.
3. **Actual GitHub URL:** sign in to Django Admin → Projects → edit each seeded project → paste the real `github_url` (the GitHub button only appears if supplied).
4. **Project summary/features:** replace the starter descriptions with precisely what your real repositories implement; remove anything that isn't accurate.
5. **Add new projects:** Admin → Projects → Add; choose a category, fill required fields, enable `is_published`.
6. **Education and work dates:** check and adjust the content before publishing publicly.
7. **Optional CV download:** later place a reviewed PDF in static files and add a download link in the hero; no made-up CV file is included.

## 7) Tests

```powershell
python manage.py test
python manage.py check
```

Tests include homepage, project detail, unpublished projects, valid contact submissions, and honeypot rejection.

## 8) Contact form behavior

The form uses Django's CSRF protection, email input validation, and a basic honeypot field. Successful submissions are **stored in the SQLite database** and can be read in Django Admin. **It does not send an email notification yet.** Before publishing, add production-grade rate limiting / spam prevention, a privacy notice and a suitable retention policy for submitted messages.

## 9) Deployment notes — not production ready as configured

- Debug mode is **ON by default for local development**. Turn it off before deploying.
- Configure strong `DJANGO_SECRET_KEY`, `DJANGO_ALLOWED_HOSTS`, HTTPS settings, persistent database, and static asset serving.
- Never commit `.env`, secrets, the local database, or `myenv/` to Git.
- Django's built-in `runserver` is only for development; choose a supported production server and hosting platform.
- For production static files: `python manage.py collectstatic` after setting up your server.
- Replace sample project descriptions with confirmed details, add a privacy policy if processing contact messages, and set up backups.

## 10) Next features after this starter

1. Blog / learning journal with models and rich content support.
2. Downloadable CV and social links (using your genuine URLs).
3. Project screenshots and image upload workflow.
4. English / Japanese content switching.
5. Deployment with domain, SEO, spam protection, email alerts, analytics.

---

This is a project starter, not a finished publicly deployed website.
