from django.conf.urls import url

from . import views

app_name = 'weatherapp'
urlpatterns = [
    url(r'^$', views.arrestDisplay, name='arrest_display_url'),
]