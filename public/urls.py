from django.conf.urls import url

from . import views

app_name = 'public'  # adding namespace to identify

urlpatterns = [
        # /public/ if app but home page is this so /
        url(r'^$', views.Indexview.as_view(), name='index'),
        url(r'^login/$', views.loginView, name='login'),
        url(r'^authenticate/$', views.authenticateView, name='authenticate'),
        url(r'^login/valid/$', views.validLoginView, name='validLogin'),
        url(r'^login/invalid/$', views.invalidLoginView, name='invalidLogin'),
        url(r'^logout/$', views.logoutView, name='logout'),
        url(r'^signup/$', views.signupView, name='signup'),
        url(r'^main/$', views.publicmainView, name='publicmain'),
        url(r'^ajaxSearch/$', views.searchView, name='search'),
        ]
