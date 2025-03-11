from django.contrib import admin
from .models import NewTask

@admin.register(NewTask)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
   