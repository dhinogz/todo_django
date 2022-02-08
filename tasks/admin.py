from django.contrib import admin
from .models import Task

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'created',)

admin.site.register(Task)