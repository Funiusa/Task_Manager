from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'created', 'status')
    search_fields = ('title', 'description')
    list_filter = ('technology', 'created', 'status')
