from django.contrib import admin

from cabinet.models import Order

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('client', 'domen')
    ordering = ['client__username']
    search_fields = ['client__username', 'domen']

admin.site.register(Order, OrdersAdmin)