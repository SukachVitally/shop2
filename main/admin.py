from django.contrib import admin
from shop.models import ProductGroup, Product, ProductInfoType, ProductGroupRelation, ProductInfo


class ProductGroupRelation(admin.TabularInline):
    model = ProductGroupRelation
    extra = 1


class ProductInfo(admin.TabularInline):
    model = ProductInfo
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductGroupRelation, ProductInfo]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGroup)
admin.site.register(ProductInfoType)
