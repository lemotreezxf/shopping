from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/(?P<good_id>\d+)/(?P<count>\d+)/$', views.add, name="add"),
    url(r'^list/$', views.list, name="list"),
    url(r'^delete/(?P<s_id>\d+)/$', views.delete, name="delete"),

]