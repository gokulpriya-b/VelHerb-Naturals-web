from django.contrib import admin
from .models import Product, Order, CustomOrder

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","category","price","is_featured","is_available")
    list_filter = ("category","is_featured","is_available")
    search_fields = ("name","ingredients")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id","customer_name","phone","total","status","is_custom","created_at")
    list_filter = ("status","is_custom","created_at")
    search_fields = ("customer_name","phone","email")
    readonly_fields = ("created_at",)

@admin.register(CustomOrder)
class CustomOrderAdmin(admin.ModelAdmin):
    list_display = ("id","customer_name","phone","product_type","quantity","status","created_at")
    list_filter = ("status","created_at")
    search_fields = ("customer_name","phone","product_type")
    readonly_fields = ("created_at",)
