from django.db import models

class Participation(models.Model):
    user = models.ForeignKey("users.user", on_delete=models.CASCADE)
    project = models.ForeignKey("projects.project", on_delete=models.CASCADE)
    dt_of_joining = models.DateField("Дата присоединения")
    dt_of_departure = models.DateField("Дата окончания")
    
    class Meta:
        verbose_name = "Участие"
        verbose_name_plural = "Участия"
        
    def __str__(self):
        return f"{self.user}"
    