# -*- coding: utf-8 -*-
from django.contrib import admin
from index import models

class SettingAdmin(admin.ModelAdmin):

    list_display = ("key","value")
    ordering = ("key",)
    search_fields = ("key","value")

admin.site.register(models.Setting,SettingAdmin)