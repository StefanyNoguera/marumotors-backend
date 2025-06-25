from django.contrib import admin
from .models import Car, Autopart

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'model', 'year', 'kilometers')

@admin.register(Autopart)
class AutopartAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'sku')
