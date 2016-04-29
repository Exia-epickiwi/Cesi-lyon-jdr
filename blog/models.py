# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from markdown import markdown
from wiki.mdExtentions import wikiMarkdownExtention
from wiki.unimoji import UnimojiExtension
from wiki.templatetags import markdown_extras

class Article(models.Model):

    title = models.CharField(max_length=255,verbose_name="Titre")
    author = models.ForeignKey(User,verbose_name="Auteur")
    content = models.TextField(verbose_name="Contenu")
    date = models.DateTimeField()
    slug = models.CharField(max_length=255,verbose_name="Slug",unique=True)

    def refreshSlug(self):
        """Définis le slug de l'article"""
        self.slug = slugify(self.title)

    def formatedContent(self):
        """Donne le texte formaté en markdown"""
        return markdown_extras.markdown(self.content)

    def __unicode__(self):
        """Donne le titre de l'article"""
        return self.title