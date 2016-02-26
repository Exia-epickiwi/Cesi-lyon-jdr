# -*- coding: utf-8 -*-
from django.conf.urls import url
from projects import views

urlpatterns = [
    url(r'^$',views.home),
    url(r'^task/(?P<id>[0-9]+)/setprogression',views.setTaskProgression),
    url(r'^(?P<slug>.+)$',views.showProject,name="project-show")
]