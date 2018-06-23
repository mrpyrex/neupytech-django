from django.shortcuts import render
from django.contrib import messages
from .models import Join
from .forms import JoinForm

# Create your views here.

def index(request):
    join = JoinForm(request.POST or None)

    if join.is_valid():
        instance = join.save(commit=False)
        if Join.objects.filter(email=instance.email).exists():
            messages.warning(request, "We have your email already",)
        else:
            instance.save()
            messages.success(request, "Thanks for Subscibing to our newsletter!")
    
    context = {'join': join,}

    return render(request, 'pages/index.html', context)

def unsubscribe(request):
    join = JoinForm(request.POST or None)
    if join.is_valid():
        instance = join.save(commit=False)
        if Join.objects.filter(email=instance.email).exists():
            Join.objects.filter(email=instance.email).delete()
        else:
            print("Sorry but we didn't find that email address")

    context = {'join': join,}

    return render(request, 'pages/unsubscribe.html', context)
    

def about(request):
    return render(request, 'pages/about.html')

def portfolio(request):
    return render(request, 'pages/portfolio.html')