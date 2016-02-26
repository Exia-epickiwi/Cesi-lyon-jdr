# -*- coding: utf-8 -*-
from django.shortcuts import render
from events.models import Event
from projects.models import Project
from wiki.models import Article
from datetime import datetime

def home(request):

    nextEvent = Event.objects.filter(date__gte=datetime.now()).order_by("date").first()
    projects = Project.objects.all()
    presentation = Article.objects.get(slug="home")

    return render(request,"index/home.html",locals())