from django.contrib import admin
from main.models import Pocket

class PocketsAdmin(admin.ModelAdmin):
    class Media:
        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', '/static/grappelli/tinymce_setup/tinymce_setup.js',]

admin.site.register(Pocket, PocketsAdmin)
