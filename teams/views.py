from django.shortcuts import render
from teams.models import Club


def index(request):
    all_teams = Club.objects.all()
    return render(request, 'teams/index.html', {'all_teams': all_teams})
