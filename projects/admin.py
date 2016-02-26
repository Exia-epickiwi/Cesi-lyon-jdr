from django.contrib import admin
from projects.models import Project, Task

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name","wikiArticle")
    ordering = ("name",)
    search_fields = ("name",)

class TaskAdmin(admin.ModelAdmin):
    list_display = ("name","progression","project")
    ordering = ("name",)
    search_fields = ("name",)

admin.site.register(Project,ProjectAdmin)
admin.site.register(Task,TaskAdmin)