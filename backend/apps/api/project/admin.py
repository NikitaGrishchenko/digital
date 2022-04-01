from apps.api.project.models import Project
from django.contrib import admin


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Project, ProjectAdmin)
