"""smallmonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# from django.conf.urls import include, url
from django.urls import path,re_path,include
from django.contrib import admin
from api import views
from smallmonitor.views import homepage, manager


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', homepage),
    re_path(r'^manager/(?P<appid>[0-9]+)/$', manager),
    re_path(r'^api/groups/$', views.group_list),
    re_path(r'^api/groups/(?P<pk>[0-9]+)/$', views.group_detail),
    re_path(r'^api/apps/$', views.app_list),
    re_path(r'^api/app/(?P<pk>.+)/$', views.app_detail),
    re_path(r'^api/mangerapp/(?P<pk>[0-9]+)/$', views.manager_detail),
    re_path(r'^api/hosts/$', views.host_list),
    re_path(r'^api/hosts/(?P<pk>[0-9]+)/$', views.host_detail),
    re_path(r'^api/history/$', views.app_history_list),
    re_path(r'^api/statistics/(?P<pk>[0-9]+)$', views.app_statistics_list),
    re_path(r'^api/count/groups/$', views.count_groups_statistics_detail),
    re_path(r'^api/count/group/(?P<pk>[0-9]+)/$', views.count_group_statistics_detail),
]

