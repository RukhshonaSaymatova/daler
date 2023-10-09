from django.db import models

class User(models.Model):
    username = models.CharField("Имя пользователя", max_length=25)
    first_name = models.CharField("Имя", max_length=25)
    last_name = models.CharField("Фамилия", max_length=25)
    email = models.EmailField("Эл.почта")
    password = models.CharField("Пароль", max_length=25)
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"  
        
    def __str__(self):
        return f"{self.username}"