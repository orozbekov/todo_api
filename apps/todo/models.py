from tabnanny import verbose
from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    task = models.CharField(verbose_name="Задача", max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    class Meta:
        verbose_name_plural = "Задачи"
        verbose_name = "Задача"

    def __str__(self):
        return self.task
