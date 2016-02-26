from django.core.exceptions import ObjectDoesNotExist

from wiki.models import Article

def getArticleBySlug(slug):
    try:
        article = Article.objects.get(slug=m.group(1))
    except ObjectDoesNotExist:
        article = None
    return article