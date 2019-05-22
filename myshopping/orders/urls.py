from django.conf.urls import url
from django.views.decorators.http import require_POST
from goods.models import Goods
from shopcart.models import ShopCart

from . import views

urlpatterns = [
    url(r'^confirm/$', views.confirm, name="confirm"),
    url(r'^pay/$', views.pay, name="pay"),
    url(r'^done/$', views.done, name="done"),
    url(r'^list/$', views.list, name="list"),
    url(r'^detail/(?P<o_id>\d+)/$', views.detail, name="detail"),
    url(r'^delete/(?P<o_id>\d+)/$', views.delete, name="delete"),

]