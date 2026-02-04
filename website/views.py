from django.shortcuts import render, get_object_or_404
from .models import Category, Project, SiteSettings
from django.core.mail import send_mail
from django.conf import settings
from .forms import InquiryForm

def home(request):
    featured_projects = (
        Project.objects
        .filter(is_featured=True, is_published=True)
        .select_related("category")
        .prefetch_related("images")[:6]
    )

    return render(request, "home.html", {
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
    settings_obj = SiteSettings.objects.first()
    success = False

    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()

            send_mail(
                subject="New Photography Inquiry",
                message=f"""
Name: {inquiry.name}
Email: {inquiry.email}

Message:
{inquiry.message}
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=True,
            )

            success = True
            form = InquiryForm()  
    else:
        form = InquiryForm()

    return render(request, "contact.html", {
        "form": form,
        "success": success,
        "settings": settings_obj,
    })
