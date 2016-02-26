# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from events import views

urlpatterns = [
    url(r'^$',views.home),
    url(r'^(?P<slug>.+)$',views.showEvent,name="event-show")
]