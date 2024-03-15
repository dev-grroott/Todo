from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=20)
    status = models.CharField(max_length=10)

    class Meta:
        db_table = "task"

    def __str__(self):
        return f"{self.name} - {self.status}"







