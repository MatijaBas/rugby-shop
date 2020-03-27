from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.


class OrderLineAdminInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )


admin.site.register(Order, OrderAdmin)
