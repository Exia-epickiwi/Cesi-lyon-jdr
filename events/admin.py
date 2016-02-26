# -*- coding: utf-8 -*-
from django.contrib import admin
from events.models import Event, Comment

# Register your models here.

class EventAdmin(admin.ModelAdmin):

    list_display = ("title","shortDescription","date","place")
    list_filter = ("place",)
    date_hierarchy = "date"
    ordering = ("date",)
    search_fields = ("title","place")

class CommentAdmin(admin.ModelAdmin):

    list_display = ("author","content","date","event")
    list_filter = ("author","event")
    date_hierarchy = "date"
    ordering = ("date",)
    search_fields = ("author","content")

admin.site.register(Event,EventAdmin)
admin.site.register(Comment,CommentAdmin)