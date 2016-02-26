# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from wiki import views

urlpatterns = [
    url(r'^$',views.home),
    url(r'^create/(?P<slug>.+)?$',views.createArticle),
    url(r'^edit/(?P<slug>.+)$',views.editArticle),
    url(r'^(?P<slug>.+)$',views.showArticle,name="wiki-show")
]