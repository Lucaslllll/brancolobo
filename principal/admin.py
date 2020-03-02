from django.contrib import admin
from .models import Product, Ingredients, Contact

admin.site.register(Product)
admin.site.register(Ingredients)
admin.site.register(Contact)