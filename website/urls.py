from django.urls import path
from . import views
from django.http import HttpResponse

def robots_txt(request):
    return HttpResponse(
        "User-agent: *\nAllow: /",
        content_type="text/plain"
    )

urlpatterns = [
    path("", views.home, name="home"),

    path("portfolio/", views.portfolio, name="portfolio"),
    path("portfolio/<slug:slug>/", views.portfolio_by_category, name="portfolio_by_category"),

    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),

    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
urlpatterns += [
    path("robots.txt", robots_txt),
]