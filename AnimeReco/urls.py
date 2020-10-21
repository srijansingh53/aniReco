
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [
    path('admin/$', admin.site.urls),
    url(r'^general/', include('general.urls')),
    url(r'^recommendation/', include('recommendation.urls')),
    url(r'^', include('general.urls')),
    
]
