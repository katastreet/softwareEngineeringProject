from django.conf.urls import url

from . import views

app_name = 'polls'  # adding a namespace to identify the urls related to app
'''
urlpatterns = [
        # /polls/
        url(r'^$', views.index, name='index'),
        # /polls/5/
        url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
        # /polls/5/results/
        url(r'(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
        # /polls/5/vote/
        url(r'(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
        ]
'''
urlpatterns = [
        # /polls/
        url(r'^$', views.IndexView.as_view(), name='index'),
        # /polls/5/
        url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
        # /polls/5/results/
        url(r'(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
        # /polls/5/vote/
        url(r'(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
        ]
