from django.db import models

# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='agents/')
    
    class Meta:
        verbose_name = ("Agent")
        verbose_name_plural = ("Agents")

    def __str__(self):
        return self.name


