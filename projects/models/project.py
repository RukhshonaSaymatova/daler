from django.db import models

class Project(models.Model):
    title = models.CharField("Название проекта", max_length=25)
    description = models.TextField("Описание", max_length=50, default="описание...")
    end_dt = models.DateField("Дата окончание")

    
    
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        
    def __str__(self):
        return f"{self.name}"