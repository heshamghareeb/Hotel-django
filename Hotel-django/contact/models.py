from django.db import models

# Create your models here.
class ContactDetails(models.Model):
    # location
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    

    class Meta:
        verbose_name = ("ContactDetails")
        verbose_name_plural = ("ContactDetailss")

    def __str__(self):
        return str(self.id)

