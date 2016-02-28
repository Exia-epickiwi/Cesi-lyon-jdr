# -*- coding: utf-8 -*-
import markdown
from django.http import Http404
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from events.models import Event
from wiki.models import Article
from datetime import datetime
from events import forms

# Create your views here.
def home(request):

    events = Event.objects.all().order_by("date").filter(date__gte=datetime.now())

    return render(request,"events/home.html",locals())

def showEvent(request,slug):

    try:
        event = Event.objects.get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404

    if request.user.is_authenticated():

        if request.method == "POST":
            form = forms.addComment(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.event = event
                comment.save()
        else:
            form = forms.addComment()

    return render(request, 'events/showEvent.html', locals())