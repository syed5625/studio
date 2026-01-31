from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("portfolio/", views.portfolio, name="portfolio"),
    path("portfolio/<slug:slug>/", views.portfolio_by_category, name="portfolio_by_category"),

    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),

    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
