from django.conf.urls import url
from ccode import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^wrong/$', views.wrong, name='wrong'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^start/$', views.start, name='start'),
    url(r'^game/(\w+)/$', views.judge, name='judge'),


]