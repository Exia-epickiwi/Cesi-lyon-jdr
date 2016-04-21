# -*- coding: utf-8 -*-
from markdown.extensions import Extension
from django.core import urlresolvers
import wiki.models
import re
from markdown.inlinepatterns import Pattern as InlinePattern
from markdown.preprocessors import Preprocessor
from django.core.exceptions import ObjectDoesNotExist
from markdown.util import etree

class inlineInternalLink(InlinePattern):
    regex = r'\[\[([^\]|]+)(\|([^\]]+))?\]\]'

    def handleMatch(self, m):
        url = urlresolvers.reverse("wiki-show",args=[m.group(2)])

        el = etree.Element("a")
        el.set("href",url)

        notFound = False

        try:
            wikiArticle = wiki.models.Article.objects.get(slug=m.group(2))
        except ObjectDoesNotExist:
            el.set("class","notFound")
            notFound = True

        if m.group(4) :
            el.text = m.group(4)
            el.set("title",m.group(4))
        elif notFound:
            el.text = m.group(2)
            el.set("title",m.group(2))
        else:
            el.text = wikiArticle.title
            el.set("title",wikiArticle.title)

        return el

class inlineProjectLink(InlinePattern):
    regex = r'!\[\[([^\]|]+)(\|([^\]]+))\]\]'

    def handleMatch(self, m):
        url = urlresolvers.reverse("project-show",args=[m.group(2)])

        el = etree.Element("a")
        el.set("href",url)

        if m.group(3) :
            el.text = m.group(4)
            el.set("title",m.group(4))
        else:
            el.text = m.group(2)
            el.set("title",m.group(4))

        return el

class inlineEventLink(InlinePattern):
    regex = r'\?\[\[([^\]|]+)(\|([^\]]+))\]\]'

    def handleMatch(self, m):
        url = urlresolvers.reverse("event-show",args=[m.group(2)])

        el = etree.Element("a")
        el.set("href",url)

        if m.group(3) :
            el.text = m.group(4)
            el.set("title",m.group(4))
        else:
            el.text = m.group(2)
            el.set("title",m.group(4))

        return el

class inlineMediaInsert(InlinePattern):
    regex = r'\$\[\[([^\]\|]+)(\|([^\]]+))?\]\]'

    def handleMatch(self, m):
        try:
            media = wiki.models.Media.objects.get(name=m.group(2))
        except ObjectDoesNotExist:
            el = etree.Element("p")
            el.text = "Image "+m.group(2)+" introuvable !"
            return el

        el = etree.Element("img")
        el.set("src",media.file.url)
        el.set("alt",media.name)
        if m.group(4):
            el.set("title",m.group(4))
        return el

class wikiMarkdownExtention(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('internallink',inlineInternalLink(inlineInternalLink.regex,md),'_end')
        md.inlinePatterns.add('projectlink',inlineProjectLink(inlineProjectLink.regex,md),'<internallink')
        md.inlinePatterns.add('eventlink',inlineEventLink(inlineEventLink.regex,md),'<projectlink')
        md.inlinePatterns.add('mediainsert',inlineMediaInsert(inlineMediaInsert.regex,md),'<eventlink')