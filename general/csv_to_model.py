from models import Anime

import pandas as pd
from django.contrib.auth import authenticate
user = authenticate(username='anireco', password='recoani')

tmp_data=pd.read_csv('anime_cleaned.csv')

anime = [
    Anime(
    		anime_id = tmp_data.ix[row]['anime_id'] ,
    		anime_name = tmp_data.ix[row]['title'] ,
    		anime_synonyms = tmp_data.ix[row]['title_synonyms'], 
    		anime_type = tmp_data.ix[row]['type'] ,
    		anime_rank = tmp_data.ix[row]['rank'] ,
    		anime_score = tmp_data.ix[row]['score'], 
    		anime_rating = tmp_data.ix[row]['rating'], 
			anime_thumbnail = tmp_data.ix[row]['image_url'], 
			anime_popularity = tmp_data.ix[row]['popularity'], 
			total_members = tmp_data.ix[row]['members'] ,
			genre = tmp_data.ix[row]['genre'] ,
			total_episodes = tmp_data.ix[row]['episodes'], 
			duration_min = int(tmp_data.ix[row]['duration_min']),
			studio = tmp_data.ix[row]['studio'] ,
			anime_premiered = tmp_data.ix[row]['premiered'],
			status = tmp_data.ix[row]['status'] 
              )
    for row in tmp_data['anime_id']
]
Anime.objects.bulk_create(anime)