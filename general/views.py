from django.shortcuts import render
from .models import Anime
import pandas as pd
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
	
	return render(request, 'general/home.html',{ 'categories':anime_list })



def top_anime(request):

    anime_list = Anime.objects.order_by('anime_rank')
    page = request.GET.get('page', 1)
    paginator = Paginator(anime_list, 5)
    try:
        anime_dict = paginator.page(page)
    except PageNotAnInteger:
    	anime_dict = paginator.page(1)
    except EmptyPage:
    	anime_dict = paginator.page(paginator.num_pages)

    return render(request, 'general/top_anime.html',{ 'categories':anime_dict })