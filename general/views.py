from django.shortcuts import render
from .models import Anime
import pandas as pd
# Create your views here.

"""
# Add data from csv to database
	tmp_data=pd.read_csv('C://Users//boltuzamaki//Desktop//animereco//aniReco//general//anime_cleaned.csv')
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
	print("Done lol")
	Anime.objects.bulk_create(anime)

	"""

def home(request):

	return render(request, 'general/home.html')

def top_anime(request):
    anime_list = Anime.objects.order_by('-anime_score')[:5]
    anime_dict = {'categories': anime_list}
    return render(request, 'general/top_anime.html', anime_dict)