from django.contrib import admin

# Register your models here.

from .models import User, Cart, Product, Shelf

admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Shelf)