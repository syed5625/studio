from django.shortcuts import render, get_object_or_404
from .models import Category, Project, SiteSettings
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def home(request):
    settings = SiteSettings.objects.first()
    featured_projects = Project.objects.filter(
        is_featured=True,
        is_published=True
    )[:3]

    return render(request, "home.html", {
        "settings": settings,
        "featured_projects": featured_projects,
    })


def portfolio(request):
    categories = Category.objects.all()
    projects = Project.objects.filter(is_published=True)

    return render(request, "portfolio.html", {
        "categories": categories,
        "projects": projects,
    })


def portfolio_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    projects = category.projects.filter(is_published=True)

    return render(request, "portfolio.html", {
        "category": category,
        "projects": projects,
    })


def project_detail(request, slug):
    project = get_object_or_404(
        Project,
        slug=slug,
        is_published=True
    )

    return render(request, "project_detail.html", {
        "project": project,
    })


def about(request):
    return render(request, "about.html")





def contact(request):
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            inquiry = form.save()

            # Send email
            send_mail(
                subject=f"New Inquiry from {inquiry.name}",
                message=inquiry.message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
            )

            success = True
            form = ContactForm()  # reset form
    else:
        form = ContactForm()

    return render(request, "contact.html", {
        "form": form,
        "success": success
    })

