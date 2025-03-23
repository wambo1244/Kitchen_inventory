from django.contrib import admin
from .models import Supplier, Ingredient, Inventory, Order

admin.site.register(Supplier)
admin.site.register(Ingredient)
admin.site.register(Inventory)
admin.site.register(Order)
