from django.shortcuts import render
from .models import Anime
# Create your views here.
def home(request):
	return render(request, 'general/home.html')

def top_anime(request):
    anime_list = Anime.objects.order_by('-anime_score')[:5]
    anime_dict = {'categories': anime_list}
    return render(request, 'general/top_anime.html', anime_dict)