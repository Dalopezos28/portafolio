from django.contrib import admin
from .models import Project, WorkExperience, Skill


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'created_at')
    list_filter = ('featured',)
    search_fields = ('title', 'description')
    list_editable = ('featured',)


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start_date', 'end_date', 'current', 'order')
    list_editable = ('order', 'current')
    ordering = ('order',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'order')
    list_editable = ('proficiency', 'order')
    list_filter = ('category',)
