from django.conf.urls import url
from . import views
from django.urls import re_path



urlpatterns = [
url(r'^$', views.home, name='home'),
url(r'^topanime/$', views.top_anime, name='top_anime'),
re_path(r'^general/(?P<anime_alphabet>[A-Z]+)/$', views.pages, name='detail'),

]