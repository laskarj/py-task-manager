from enum import StrEnum, auto

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Priority(StrEnum):
    URGENT = auto()
    HIGH = auto()
    LOW = auto()


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name", ]


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_DEFAULT,
        related_name="workers",
        default=None,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}({self.position})"


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=6,
        choices=[(priority.value, priority.name) for priority in Priority]
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    workers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tasks"
    )
