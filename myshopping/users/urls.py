from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^register/$', views.register, name="register"),
    url(r'^logout/$', views.user_logout, name="user_logout"),
    url(r'^code/$', views.code, name="code"),
    url(r'^info/$', views.info, name="info"),
    url(r'^edit/$', views.edit, name="edit"),
    url(r'^editpwd/$', views.editpwd, name="editpwd"),
    url(r'^check_user/$', views.check_user, name="check_user"),
    url(r'^check_login/$', views.check_login, name="check_login"),

]