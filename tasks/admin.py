from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Worker, Task, TaskType, Position


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", )
    fieldsets = UserAdmin.fieldsets + (
        (
            "Information", {"fields": ("position", )}
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Information", {
                "fields": (
                    "first_name", "last_name", "position",
                ),
            }
        ),
    )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "name", "deadline", "priority", "is_completed", "task_type"
    ]

admin.site.register(TaskType)
admin.site.register(Position)
