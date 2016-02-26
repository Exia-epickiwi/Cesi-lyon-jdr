# -*- coding: utf-8 -*-
from django.contrib import admin
from wiki.models import Article, Redirection, Message, Modification

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","creation")
    date_hierarchy = "creation"
    ordering = ("creation",)
    search_fields = ("title",)

class RedirectionAdmin(admin.ModelAdmin):
    list_display = ("slug","article")
    list_filter = ("article",)
    ordering = ("slug",)
    search_fields = ("slug","article")

class MessageAdmin(admin.ModelAdmin):
    list_display = ("author","content","article","date")
    list_filter = ("author",)
    ordering = ("date",)
    date_hierarchy = "date"
    search_fields = ("content","author","article")

class ModificationAdmin(admin.ModelAdmin):
    list_display = ("article","author","date")
    list_filter = ("author","article")
    ordering = ("date",)
    date_hierarchy = "date"
    search_fields = ("author","article","newContent")


admin.site.register(Article,ArticleAdmin)
admin.site.register(Redirection,RedirectionAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register(Modification,ModificationAdmin)