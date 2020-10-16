from django.conf.urls import url
from . import views



urlpatterns = [
url(r'^general/', views.home, name='home'),
url(r'^topanime/', views.top_anime, name='top_anime'),
url(r'^', views.home, name='home'),

]