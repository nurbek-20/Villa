from django.contrib import admin
from .models import Category, PaymentMethod, Material, Villa, Storage

admin.site.register(Category)
admin.site.register(PaymentMethod)
admin.site.register(Material)
admin.site.register(Villa)
admin.site.register(Storage)
