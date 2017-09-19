from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	# context = {
	# 	"leagues": League.objects.all(),
	# 	"teams": Team.objects.all(),
	# 	"players": Player.objects.all(),
	# }


	context = {
		"mleagues": League.objects.filter(sport = 'Baseball'),
		"wleagues": League.objects.filter(name__icontains = 'Women'),
		"hleagues": League.objects.filter(sport__icontains = 'Hockey'),
		"nothleagues": League.objects.exclude(sport__icontains = 'Hockey'),
		"confleagues": League.objects.filter(name__icontains = 'Conference'),
		"aleagues": League.objects.filter(name__icontains = 'Atlantic'),
		"teams": Team.objects.all(),
		"dteams": Team.objects.filter(location = 'Dallas'),
		"rteams": Team.objects.filter(team_name__icontains = 'Raptors'),
		"cityteams": Team.objects.filter(location__contains = 'City'),
		"Tstartteams": Team.objects.filter(location__startswith = 'T'),
		"locteams": Team.objects.all().order_by('-location'),
		"players": Player.objects.all(),
		"coopplayers": Player.objects.filter(last_name='Cooper'), 
		"joshuaplayers": Player.objects.filter(first_name='Joshua'),
		"jcplayers":Player.objects.filter(last_name='Cooper') & Player.objects.filter(first_name='Joshua'),
		"awplayers": Player.objects.filter(first_name='Alexander') | Player.objects.filter(first_name='Wyatt')
	
	}
	
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")