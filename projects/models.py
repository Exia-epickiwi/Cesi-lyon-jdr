# -*- coding: utf-8 -*-
from django.db import models
from wiki import models as wikiModels
from django.utils.text import slugify
import math

class Project(models.Model):

    name = models.CharField(max_length=255,verbose_name="Nom")
    wikiArticle = models.ForeignKey(wikiModels.Article,verbose_name="Article de description")
    slug = models.CharField(max_length=255,verbose_name="Identifiant")

    def __unicode__(self):
        """Renvoie le nom du projet"""

        return self.name

    def refreshSlug(self):
        self.slug = slugify(self.title)

    def tasks(self):
        """Renvoie les taches du projet"""

        return self.task_set.all()

    def progression(self):
        """Calcule la moyenne des progressions des taches"""

        average = 0

        for task in self.task_set.all():
            average += task.progression

        average /= self.task_set.all().count()

        average = math.trunc(average)

        return average

class Task(models.Model):

    name = models.CharField(max_length=255,verbose_name="Nom")
    progression = models.IntegerField(verbose_name="Progression")
    project = models.ForeignKey(Project,verbose_name="Projet associé")

    def __unicode__(self):
        """Renvoie le nom de la tache"""

        return self.name