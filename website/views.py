from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings as django_settings

from .models import Category, Project, SiteSettings
from .forms import InquiryForm


def get_site_settings():
    return SiteSettings.objects.first()


def home(request):
    context = {
        "settings": get_site_settings(),
        "featured_projects": Project.objects.filter(
            is_featured=True,
            is_published=True
        ),
        "categories": Category.objects.all(),
    }
    return render(request, "home.html", context)


def portfolio(request):
    context = {
        "categories": Category.objects.all(),
        "projects": Project.objects.filter(is_published=True),
    }
    return render(request, "portfolio.html", context)


def portfolio_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    context = {
        "category": category,
        "projects": category.projects.filter(is_published=True),
    }
    return render(request, "portfolio.html", context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, is_published=True)
    return render(request, "project_detail.html", {"project": project})


def about(request):
    return render(request, "about.html", {"settings": get_site_settings()})


def contact(request):
    site_settings = get_site_settings()
    success = False

    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()

            send_mail(
                "New Photography Inquiry",
                f"Name: {inquiry.name}\nEmail: {inquiry.email}\n\n{inquiry.message}",
                django_settings.DEFAULT_FROM_EMAIL,
                [django_settings.CONTACT_EMAIL],
                fail_silently=True,
            )

            success = True
            form = InquiryForm()
    else:
        form = InquiryForm()

    return render(request, "contact.html", {
        "form": form,
        "success": success,
        "settings": site_settings,
    })
