from django.conf.urls import url
from . import views
from django.urls import re_path

app_name = 'general'

urlpatterns = [
url(r'^$', views.home, name='home'),
url(r'^home/$', views.home, name='home'),
url(r'^top_anime/$', views.top_anime, name='top_anime'),
url(r'^genre/$', views.genre, name='genre'),
re_path(r'^(?P<anime_alphabet>[A-Z]+)/$', views.pages, name='detail'),

]