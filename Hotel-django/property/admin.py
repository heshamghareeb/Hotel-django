from django.contrib import admin
from .models import Property,Category,Reserve

# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name' , 'property_type' , 'category' , 'area' , 'beds_number' , 'baths_number' , 'garages_number']
    search_fields = ['name' , 'property_type']
    list_filter = ['category' , 'property_type']


admin.site.register(Property, PropertyAdmin)
admin.site.register(Category)
admin.site.register(Reserve)