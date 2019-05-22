from django.conf.urls import url

from .import views

urlpatterns=[
    url(r'^add/$', views.add, name='add'),
    url(r'^findType/$', views.findType, name='findType'),
    url(r'^detail/(?P<g_id>\d+)/$', views.detail, name='detail'),
    url(r'^delete/(?P<g_id>\d+)/$', views.delete, name="delete"),

]