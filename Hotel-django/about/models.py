from django.db import models

# Create your models here.
class About(models.Model):
    vision = models.TextField()
    mission = models.TextField()
    image = models.ImageField(upload_to='about/')

    class Meta:
        verbose_name = ("About")
        verbose_name_plural = ("Abouts")

    def __str__(self):
        return str(self.id)

