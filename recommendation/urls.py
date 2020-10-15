from django.conf.urls import url
from . import views



urlpatterns = [
url(r'^recommendation/', views.home, name='home'),
url(r'^', views.home, name='home'),
]