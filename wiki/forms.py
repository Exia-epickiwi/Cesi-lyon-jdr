# -*- coding: utf-8 -*-
from django import forms
from wiki.models import Article, Message

class CreateArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ("title","content")

class EditArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ("content",)

class AddMessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ("content",)