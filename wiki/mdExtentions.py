# -*- coding: utf-8 -*-
from markdown.extensions import Extension
from django.core import urlresolvers
import re
from markdown.inlinepatterns import Pattern as InlinePattern
from markdown.preprocessors import Preprocessor
from django.core.exceptions import ObjectDoesNotExist
from markdown.util import etree

class inlineInternalLink(InlinePattern):
    regex = r'\[\[([^\]|]+)(\|([^\]]+))\]\]'

    def handleMatch(self, m):
        url = urlresolvers.reverse("wiki-show",args=[m.group(2)])

        el = etree.Element("a")
        el.set("href",url)

        if m.group(3) :
            el.text = m.group(4)
            el.set("title",m.group(4))
        else:
            el.text = m.group(2)
            el.set("title",m.group(4))

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

class wikiMarkdownExtention(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('internallink',inlineInternalLink(inlineInternalLink.regex,md),'_end')
        md.inlinePatterns.add('projectlink',inlineProjectLink(inlineProjectLink.regex,md),'<internallink')
        md.inlinePatterns.add('eventlink',inlineEventLink(inlineEventLink.regex,md),'<projectlink')