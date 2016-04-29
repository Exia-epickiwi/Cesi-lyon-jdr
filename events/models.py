# -*- coding: utf-8 -*-
from django.db import models
from markdown import markdown
from django.contrib.auth.models import User
from wiki.mdExtentions import wikiMarkdownExtention
from wiki.unimoji import UnimojiExtension

# Create your models here.
class Event(models.Model):

    title = models.CharField(max_length=255,verbose_name="Titre")
    slug = models.CharField(max_length=255,verbose_name="Identifiant",unique=True)
    description = models.TextField(verbose_name="Description")
    date = models.DateTimeField(verbose_name="Date")
    place = models.CharField(max_length=255,verbose_name="Lieu")
    shortDescription = models.CharField(max_length=255,verbose_name="Courte description")
    background = models.ImageField(verbose_name="Arrière plan",blank=True,null=True,upload_to="eventsBackgrounds/")

    def formatedDescription(self):
        content = markdown(self.content,extensions=[wikiMarkdownExtention(),UnimojiExtension()])

    def comments(self):
        return self.comment_set.all().order_by("date")

    def commentNumber(self):
        return len(self.comments())

    def __unicode__(self):
        """Renvoie le titre de l'evenement"""

        return self.title

class Comment(models.Model):

    author = models.ForeignKey(User,blank=True,null=True,verbose_name="Auteur")
    authorName = models.CharField(max_length=255,blank=True,null=True,verbose_name="Nom",help_text="Si l'auteur n'est pas un utilisateur")
    content = models.TextField(verbose_name="Contenu")
    date = models.DateTimeField(auto_now_add=True,verbose_name="Date")
    event = models.ForeignKey(Event,verbose_name="Evenement associé")

    def __unicode__(self):
        """Renvoie le contenu du commentaire"""

        return self.content