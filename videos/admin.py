from django.contrib import admin

# Register your models here.
from .models import Video, VideoAdmin

# Register your models here.
admin.site.register(Video, VideoAdmin)