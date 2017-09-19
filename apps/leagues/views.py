from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker
from django.db.models import Q
from django.db.models import Count

def index(request):
	# context = {
	# 	"leagues": League.objects.all(),
	# 	"teams": Team.objects.all(),
	# 	"players": Player.objects.all(),
	# }


	context = {
		# All Teams in the Atlantic Soccer Conference
		"ateams": Team.objects.filter(league__name = 'Atlantic Soccer Conference'),
		# Penguin Players
		"Bplayers": Player.objects.filter(curr_team__team_name = 'Penguins'),
		# International Collegiate Baseball Conference Players
		"Iplayers": Player.objects.filter(curr_team__league_id=2),

		# American Conference of Amateur Football + Last name Lopez<
		"Lplayers": Player.objects.filter(curr_team__league_id=7) & Player.objects.filter(last_name="Lopez"),
		
		# All Football Players
		"fplayers": Player.objects.filter(curr_team__league_id=7) | Player.objects.filter(curr_team__league_id=9),
		'fteams': Team.objects.filter(league__sport="Football"),
		# All teams with player named Sophia
		'steams': Team.objects.filter(all_players__first_name="Sophia"),

		# all leagues with player named Sophia
		'sleague': League.objects.filter(teams__id=25) | League.objects.filter(teams__id=4) | League.objects.filter(teams__id=32),  
		# everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders
		"notfplayers": Player.objects.filter(last_name = 'Flores') & Player.objects.filter(~Q(curr_team_id=10)) ,
		# all teams, past and present, that Samuel Evans has played with
		'seteams': Team.objects.filter(all_players__id=115),
		# All players, past and present, with the Manitoba Tiger-Cats

		"maniplayers": Player.objects.filter(all_teams__id=4),
		# ll players who were formerly (but aren't currently) with the Wichita Vikings
		"vikiplayers": Player.objects.filter(all_teams__id=40),
		# all teams, past and present, that Samuel Evans has played with<
		'jacteams': Team.objects.filter(all_players__id=151)[:3],
		# everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Playerss
		"atplayers": Player.objects.filter(first_name="Joshua") & Player.objects.filter(all_teams__league_id=3),
		# all players that have 12 or more players
		"playerNums": Team.objects.annotate(nplayer=Count('all_players')).filter(nplayer__gt=12),
		# all players and count of teams played for, sorted by the number of teams they've played for
		"allplayerteam": Team.objects.annotate(nplayer=Count('all_players')).order_by('nplayer')
	
	}
	
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")