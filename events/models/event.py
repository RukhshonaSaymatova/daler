from django.db import models

class Event(models.Model):
    title = models.CharField("Название события", max_length=25)
    description = models.TextField("Описание", max_length=50, default="описание ....")
    date = models.DateField("Дата события")
    location = models.CharField("Местоположение события", max_length=50)
    
    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
        
    def __str__(self):
        return f"{self.title}"