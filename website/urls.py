from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('category/<str:category>/', views.category, name='category'),
    path('project/', views.project_detail, name='project'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
