from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/$', views.add, name="add"),
    url(r'^list/$', views.list, name="list"),
    url(r'^update/(?P<s_id>\d+)/$', views.update, name="update"),
    url(r'^delect/(?P<s_id>\d+)/$', views.delect, name="delect"),
    url(r'^detail/(?P<s_id>\d+)/$', views.detail, name="detail"),
    url(r'^close/(?P<s_id>\d+)/$', views.close, name="close"),
]