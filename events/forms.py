# -*- coding: utf-8 -*-
from django import forms
from events import models

class addComment(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = ("content",)

class addAnoymousComment(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = ("authorName","content")