# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-28 18:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20160428_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'Auteur'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='authorName',
            field=models.CharField(blank=True, help_text=b"Si l'auteur n'est pas un utilisateur", max_length=255, null=True, verbose_name=b"Nom de l'auteur"),
        ),
    ]
