from django.conf.urls import url

from . import views

urlpatterns = [
        # /public/ if app but home page is this so /
        url(r'^$', views.Indexview.as_view(), name='index'),
        ]
