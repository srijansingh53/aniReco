from django.shortcuts import render
from .models import Anime
import pandas as pd
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q, Subquery

# Create your views here.

"""
# Add data from csv to database
	tmp_data=pd.read_csv('C://Users//boltuzamaki//Desktop//animereco//aniReco//general//databse_add.csv')
	try:
		anime = [
		Anime(
	    		anime_id = tmp_data.iloc[row]['anime_id'] ,
	    		anime_name = tmp_data.iloc[row]['title'] ,
	    		anime_synonyms = tmp_data.iloc[row]['title_synonyms'], 
	    		anime_type = tmp_data.iloc[row]['type'] ,
	    		anime_rank = tmp_data.iloc[row]['rank'] ,
	    		anime_score = tmp_data.iloc[row]['score'], 
	    		anime_rating = tmp_data.iloc[row]['rating'], 
				anime_thumbnail = tmp_data.iloc[row]['image_url'], 
				anime_popularity = tmp_data.iloc[row]['popularity'], 
				total_members = tmp_data.iloc[row]['members'] ,
				genre = tmp_data.iloc[row]['genre'] ,
				total_episodes = tmp_data.iloc[row]['episodes'], 
				duration_min = tmp_data.iloc[row]['duration_min'],
				studio = tmp_data.iloc[row]['studio'] ,
				anime_premiered = tmp_data.iloc[row]['premiered'],
				status = tmp_data.iloc[row]['status'] 
				)
		for row in range(0, len(tmp_data))
		]
	except:
		print("lol")
	Anime.objects.bulk_create(anime)

	"""


def home(request):
	anime_list = [Anime.objects.filter(anime_name__istartswith=i) for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
	return render(request, 'general/home.html',{ 'categories':anime_list[0][:18] })


def top_anime(request):
	anime_list = Anime.objects.order_by('anime_rank')
	page = request.GET.get('page', 1)
	paginator = Paginator(anime_list, 18)
	try:
		anime_dict = paginator.page(page)
	except PageNotAnInteger:
		anime_dict = paginator.page(1)
	except EmptyPage:
		anime_dict = paginator.page(paginator.num_pages)
	return render(request, 'general/top_anime.html',{ 'categories':anime_dict })


def genre(request):
	genrename = ["Comedy","Supernatural","Romance","Shounen","Parody","School","Magic","Shoujo","Drama",  \
    "Fantasy","Kids","Action","Music","SliceofLife","Josei","Harem","ShounenAi","Adventure","SuperPower","Sci-Fi",   \
    "Ecchi","Seinen","MartialArts","Game","Sports","Demons","Historical","Horror","Mystery","Psychological",      \
    "Vampire","Mecha","Military","Space","Samurai","Thriller","Hentai","Yaoi","ShoujoAi","Police","Cars",       \
    "Dementia","Yuri"]
	lists = []
	for gen in genrename:
		if request.GET.get(str(gen), 'off') == "on":
			lists.append(gen)
	context = { 'genrename':genrename }

	try:
		anime_dict = Anime.objects.filter(genre__in=lists)
		#print(lists)
		#print(anime_dict)
		page = request.GET.get('page', 1)
		paginator = Paginator(anime_dict, 18)
    try:
			anime_dict = paginator.page(page)
		except PageNotAnInteger:
			anime_dict = paginator.page(1)
		except EmptyPage:
			anime_dict = paginator.page(paginator.num_pages)
    context = { 'genrename':genrename ,'categories':anime_dict }
     
	except:
		pass		
	return render(request, 'general/genre.html', context)

def pages(request, anime_alphabet):
	if request.method == 'GET':
		if anime_alphabet=='all':
			anime_list = Anime.objects.all()
			page = request.GET.get('page', 1)
			paginator = Paginator(anime_list, 18)

		elif anime_alphabet=='misc':
			anime_list = Anime.objects.exclude(anime_name__regex=r'^[a-zA-Z]')
			page = request.GET.get('page', 1)
			paginator = Paginator(anime_list, 18)

		else:
			anime_list = Anime.objects.filter(anime_name__istartswith=str(anime_alphabet))
			page = request.GET.get('page', 1)
			paginator = Paginator(anime_list, 18)

		try:
			anime_dict = paginator.page(page)
		except PageNotAnInteger:
			anime_dict = paginator.page(1)
		except EmptyPage:
			anime_dict = paginator.page(paginator.num_pages)
      
		return render(request, 'general/home.html',{ 'categories':anime_dict })
  