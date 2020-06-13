from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import User, Cart, Product, Shelf

admin.site.register(User, UserAdmin)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Shelf)