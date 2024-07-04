from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_filter = (
        'name', 'price'
    )
    list_editable = (
        'price',
    )

admin.site.register(
    Product, ProductAdmin
)