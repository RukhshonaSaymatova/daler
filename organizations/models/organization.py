from django.db import models

class Organization(models.Model):
    name = models.CharField("Название организации", max_length=25)
    description = models.TextField("Описание", max_length=50, default="описание...")
    project = models.ForeignKey("projects.project", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
        
    def __str__(self):
        return f"{self.name}"