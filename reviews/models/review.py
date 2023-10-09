from django.db import models

class Review(models.Model):
    user = models.ForeignKey("users.user", on_delete=models.CASCADE)
    project = models.ForeignKey("projects.project", on_delete=models.CASCADE)
    reviews_text = models.TextField("Текст")
    class Rating(models.TextChoices):
        ONE = "ONE", "1"
        TWO = "TWO", "2"
        THREE = "THREE", "3"
        FOUR = "FOUR", "4"
        FIVE = "FIVE", "5"
    rating = models.CharField("Рейтинг", choices=Rating.choices, default=Rating.ONE, max_length=20)
    
    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
        
    def __str__(self):
        return f"{self.rating}"
    
