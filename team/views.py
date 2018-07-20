from django.shortcuts import render
from .models import Team

# Create your views here.
def team(request):
    persons = Team.objects.all()
    context = {'persons' : persons}
    return render(request, 'team/team.html', context)