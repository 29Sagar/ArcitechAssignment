from django.contrib import admin

from student.models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title","description","status")
    search_fields = ("title",)

admin.site.register(Task,TaskAdmin)