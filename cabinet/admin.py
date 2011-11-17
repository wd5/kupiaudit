from django.contrib import admin

from cabinet.models import Order

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('client', 'domen')
    ordering = ['client__username']
    search_fields = ['client__username', 'domen']

    class Media:
        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', '/static/grappelli/tinymce_setup/tinymce_setup.js',]

admin.site.register(Order, OrdersAdmin)