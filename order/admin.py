from django.contrib import admin
from .models import Table, Category, Menu, OrderInfo, OrderDetail


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    pass


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    pass
