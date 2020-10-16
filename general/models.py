from django.db import models


class Anime(models.Model):
	ALL_SEASONS = [
	("WINTER", 'Winter'),
	("SPRING", 'Spring'),
	("FALL", 'Fall'),
	("SUMMER", 'Summer')]

	SHOW_STATUS = [
	("RUNNING", 'Running'),    
	("COMPLETED", 'Completed')]

	anime_id = models.IntegerField()
	anime_name = models.CharField(max_length=100)
	anime_synonyms = models.CharField(max_length=300)
	anime_type = models.CharField(max_length=50)
	anime_rank = models.IntegerField()
	anime_score = models.DecimalField(max_digits=4, decimal_places=2)
	anime_rating = models.CharField(max_length=100)
	anime_thumbnail = models.CharField(max_length=500)
	anime_popularity = models.IntegerField(default=0)
	total_members = models.IntegerField(default=0)
	synopsis = models.CharField(max_length=1000)
	genre = models.CharField(max_length=200)
	total_episodes = models.IntegerField(default=0)
	duration_min = models.DecimalField(max_digits=4, decimal_places=2)
	studio = models.CharField(max_length=200)
	start_season = models.CharField(
		max_length=9,
		choices=ALL_SEASONS,
		default="WINTER",
		)
	start_year = models.IntegerField()
	status = models.CharField(
		max_length=9,
		choices=SHOW_STATUS,
		default="RUNNING",)
	def __str__(self):
		return self.anime_name