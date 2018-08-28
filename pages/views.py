from django.shortcuts import render

from newsletter.models import Join
from newsletter.forms import JoinForm

# Create your views here.

def index(request):  
    form = JoinForm()
    context = {
        'title': 'Home',
        'form': form,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    context = {
        'title': 'About Us',
    }
    return render(request, 'pages/about.html', context)

def portfolio(request):
    context = {
        'title': 'Our Works',
    }
    return render(request, 'pages/portfolio.html', context)