from django.shortcuts import render
from django.http import HttpResponse
from .models import Serie, Season, Episode

def series(request):
	context = {'series': Serie.objects.all()}
	return render(request, 'series/series.html', context)

def seasons(request, serie_id):
	context = {'seasons': Season.objects.filter(serie=serie_id).values()}
	return render(request, 'series/season.html', context)

def episodes(request, serie_id, season_id):
	context = {'episodes': Episode.objects.filter(serie=serie_id, season=season_id)}

	return render(request, 'series/episode.html', context)