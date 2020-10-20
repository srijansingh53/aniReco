from django.db import models


class Anime(models.Model):
	anime_id = models.IntegerField(primary_key = True)
	anime_name = models.CharField(max_length=100,default="Missing")
	anime_synonyms = models.CharField(max_length=300, default="Missing")
	anime_type = models.CharField(max_length=50, default="Missing")
	anime_rank = models.CharField(max_length=8, default="Missing")
	anime_score = models.CharField(max_length=5, default="Missing")
	anime_rating = models.CharField(max_length=100,default="Missing")
	anime_thumbnail = models.CharField(max_length=500)
	anime_popularity = models.IntegerField(default=0)
	total_members = models.IntegerField(default=0)
	genre = models.CharField(max_length=200,default="Missing")
	total_episodes = models.IntegerField(default=0)
	duration_min = models.CharField(max_length=8, default="Missing")
	studio = models.CharField(max_length=200,default="Missing")
	anime_premiered = models.CharField(max_length=10,default="Missing")
	status = models.CharField(max_length=8,default="Missing")

	def __str__(self):
		return self.anime_name