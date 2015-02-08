from django.contrib import admin
from main.models import ProductGroup, Product

class ProductInline(admin.StackedInline):
    model = Product
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

admin.site.register(ProductGroup, ProductAdmin)