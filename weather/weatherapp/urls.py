from django.conf.urls import url

from . import views

app_name = 'weatherapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^result', views.result, name='result'),
    url(r'^singleResult', views.singleResult, name='singleResult'),
    url(r'^searchByWeatherType', views.searchByWeatherType, name='searchByWeatherType'),
    url(r'^weatherTypeResponse', views.weatherTypeResponse, name='weatherTypeResponse'),
    url(r'^arrests', views.arrestDisplay, name='arrest_display_url')
]