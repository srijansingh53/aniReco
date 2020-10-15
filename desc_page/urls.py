from django.conf.urls import url
from . import views

urlpatterns = [
url('', views.description_page, name='description'),
]