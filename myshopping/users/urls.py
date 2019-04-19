from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^register/$', views.register, name="register"),
    url(r'^logout/$', views.user_logout, name="user_logout"),
    url(r'^code/$', views.code, name="code"),
    url(r'^check_user/$', views.check_user, name="check_user"),

]