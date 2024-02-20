from django.db import models
from django.contrib import admin

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(null=True)
    note = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class VideoAdmin(admin.ModelAdmin):
    list_display = ["name", "link", "note"]
    search_fields = ["name",  "link", "note"]
    ordering = ["name", "note"]
    readonly_fields = ("created","updated",)