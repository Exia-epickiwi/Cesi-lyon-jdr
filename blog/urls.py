# -*- coding: utf-8 -*-
from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^flux\.rss$',views.rss),
]