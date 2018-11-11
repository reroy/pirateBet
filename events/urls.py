from django.conf.urls import url

from . import views

app_name = 'events'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<match_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<match_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<match_id>[0-9]+)/bet/$', views.bet, name='bet'),
]