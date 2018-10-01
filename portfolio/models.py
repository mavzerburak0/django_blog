from django.db import models

# Create your models here.
class PortfolioItem(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
