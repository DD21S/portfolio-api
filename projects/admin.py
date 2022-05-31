from django.contrib import admin

from projects.models import Project, Tag

# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_published',)
    list_filter = ('date_published',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
