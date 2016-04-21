# -*- coding: utf-8 -*-
from django import template
from markdown import markdown
from wiki.mdExtentions import wikiMarkdownExtention
from wiki.unimoji import UnimojiExtension


register = template.Library()

def markdown_tag(text):
    """Renvoie un texte formaté en markdown avec toutes les extentions du site"""

    content = markdown(text,extensions=[wikiMarkdownExtention(),UnimojiExtension()])
    return content

register.filter('markdown',markdown_tag)