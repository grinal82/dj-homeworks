from django.contrib import admin

from logistic.models import Product, Stock, StockProduct

class StockProductInline(admin.TabularInline):
    model = StockProduct

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    
    
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    inlines = [StockProductInline]
    list_display = ('id', 'address')
