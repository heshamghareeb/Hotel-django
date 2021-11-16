from django.db import models
from django.db.models.fields import DecimalField, PositiveIntegerField

# Create your models here.
property_type = (
    ('sale' , "sale"),
    ('rent' , "rent")
    )


class Property(models.Model):
    name = models.CharField(("name"), max_length=50)
    location = models.CharField(("location"), max_length=50, null=True)
    area = models.DecimalField(decimal_places=2,max_digits=8)
    property_type = models.CharField(choices=property_type,max_length=10)
    category = models.ForeignKey('Category', null=True,on_delete=models.SET_NULL)
    price = models.PositiveIntegerField(("price"))
    beds_number = models.PositiveIntegerField(("beds"))
    baths_number = models.PositiveIntegerField(("baths"))
    garages_number = models.PositiveIntegerField(("garages"))
    image = models.ImageField(("image"), upload_to='property/',null=True)

    class Meta:
        verbose_name = ("Property")
        verbose_name_plural = ("Properties")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Property_detail", kwargs={"pk": self.pk})

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category/')
    

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.category_name


class Reserve(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    notes  = models.TextField()

    def __str__(self):
        return self.name