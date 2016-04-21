# -*- coding: utf-8 -*-
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from markdown import markdown
from wiki.mdExtentions import wikiMarkdownExtention

class Article(models.Model):

    title = models.CharField(max_length=255,verbose_name="Titre")
    slug = models.CharField(max_length=255,verbose_name="Identifiant")
    content = models.TextField(null=True,verbose_name="Contenu")
    creation = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name="Date de creation")

    def refreshSlug(self):
        self.slug = slugify(self.title)

    def formatedContent(self):
        content = markdown(self.content,extensions=[wikiMarkdownExtention()])
        return content

    def baseMessages(self):
        return self.message_set.filter(reply=None).order_by("date")

    def makeModification(self,author):
        """Crée une instance Modification avec le contenu actuel"""

        modif = Modification()
        modif.author = author
        modif.newContent = self.content
        modif.article = self
        modif.save()

    def __unicode__(self):
        """Renvoie le titre de l'article"""

        return self.title

class Modification(models.Model):

    article = models.ForeignKey(Article,verbose_name="Article réfèrant")
    author = models.ForeignKey(User,verbose_name="Utilisateur")
    newContent = models.TextField(verbose_name="Contenu modifié")
    date = models.DateTimeField(auto_now_add=True,verbose_name="Date")

    def __unicode__(self):
        """Renvoie l'auteur de la modification"""

        return "Modification de "+self.article.__unicode__()+" par "+self.author.username

class Redirection(models.Model):

    slug = models.CharField(max_length=255,verbose_name="Identifiant")
    article = models.ForeignKey(Article,verbose_name="Article cible")

    def __unicode__(self):
        """Renvoie le slug"""

        return self.slug

class Message(models.Model):

    author = models.ForeignKey(User,verbose_name="Auteur")
    content = models.TextField(verbose_name="Contenu")
    date = models.DateTimeField(auto_now_add=True,verbose_name="Date")
    article = models.ForeignKey(Article,verbose_name="Article associé")
    reply = models.ForeignKey('self',verbose_name="Message de base",default=None,null=True)

    def __unicode__(self):
        """Renvoie le contenu"""

        return self.content

    def replys(self):

        return self.message_set.order_by("date")

class Media(models.Model):

    author = models.ForeignKey(User,verbose_name="Auteur")
    file = models.ImageField(verbose_name="Média",upload_to="wikiMedia/")
    name = models.CharField(max_length=255,verbose_name="Nom",unique=True)
    uploadDate = models.DateTimeField(verbose_name="Date d'upload",auto_now_add=True)

    def __unicode__(self):
        """Donne le nom du media"""
        return self.name