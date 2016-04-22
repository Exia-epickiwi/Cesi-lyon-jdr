from datetime import datetime

from django.shortcuts import render
from blog.models import Article

def rss(request):
    articles = Article.objects.filter(date__lte=datetime.now()).order_by("-date")
    return render(request, "blog/flux.rss", locals(),content_type="application/rss+xml")
