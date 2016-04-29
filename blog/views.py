from datetime import datetime

from django.shortcuts import render
from blog.models import Article
import events.forms as forms

def rss(request):
    articles = Article.objects.filter(date__lte=datetime.now()).order_by("-date")
    return render(request, "blog/flux.rss", locals(),content_type="application/xml")

def showArticle(request,slug):
    article = Article.objects.get(slug=slug)
    comments = article.comment_set.all()

    if request.user.is_authenticated():

        if request.method == "POST":
            form = forms.addComment(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.blogArticle = article
                comment.save()
        form = forms.addComment()

    else:

        if request.method == "POST":
            form = forms.addAnoymousComment(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.blogArticle = article
                comment.save()
        form = forms.addAnoymousComment()

    return render(request, "blog/showArticle.html",locals())