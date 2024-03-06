from django.db import models
from django.contrib.auth.models import AbstractUser


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
        default=None
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}({self.position})"
