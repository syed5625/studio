from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def category(request, category):
    return render(request, 'portfolio.html', {
        'selected_category': category
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def project_detail(request):
    return render(request, 'project_detail.html')
