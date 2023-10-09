from django.db import models

class Task(models.Model):
    title = models.CharField("Название задачи", max_length=25)
    description = models.TextField("Описание задачи", max_length=50, default="описание...")
    project = models.ForeignKey("projects.project", on_delete=models.CASCADE)
    class Status(models.TextChoices):
        pending = " В ожидании"
        completed = "Выполнена"
        in_progress = "В процессе"
        canceled = "Отменено"
        
    status = models.CharField("Статус", choices=Status.choices, default=Status.pending, max_length=20) 
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        
    def __str__(self):
        return f"{self.title}"
