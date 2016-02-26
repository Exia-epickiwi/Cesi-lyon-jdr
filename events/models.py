# -*- coding: utf-8 -*-
from django.db import models
from markdown import markdown

# Create your models here.
class Event(models.Model):

    title = models.CharField(max_length=255,verbose_name="Titre")
    slug = models.CharField(max_length=255,verbose_name="Identifiant")
    description = models.TextField(verbose_name="Description")
    date = models.DateTimeField(verbose_name="Date")
    place = models.CharField(max_length=255,verbose_name="Lieu")
    shortDescription = models.CharField(max_length=255,verbose_name="Courte description")
    background = models.ImageField(verbose_name="Arrière plan",blank=True,null=True,upload_to="eventsBackgrounds/")

    def formatedDescription(self):
        return markdown(self.description)

    def comments(self):
        return self.comment_set.all().order_by("date")

    def commentNumber(self):
        return len(self.comments())

    def __unicode__(self):
        """Renvoie le titre de l'evenement"""

        return self.title

class Comment(models.Model):

    author = models.CharField(max_length=255,verbose_name="Auteur")
    content = models.TextField(verbose_name="Contenu")
    date = models.DateTimeField(auto_now_add=True,verbose_name="Date")
    event = models.ForeignKey(Event,verbose_name="Evenement associé")

    def __unicode__(self):
        """Renvoie le contenu du commentaire"""

        return self.content