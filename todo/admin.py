from django.contrib import admin
from .models import Task


class Taskadmin(admin.ModelAdmin):
    list_display=('task','is_completed','modified_at')
    search_fields=('task',)
# Register your models here.
admin.site.register(Task,Taskadmin)

