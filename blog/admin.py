# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","author","date")
    date_hierarchy = "date"
    ordering = ("date",)
    search_fields = ("title","author","content")

admin.site.register(Article,ArticleAdmin)
