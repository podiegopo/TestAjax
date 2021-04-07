from django.contrib import admin
from .models import datos

class datosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'cantidad')
    search_fields = ('nombre', 'categoria')
    list_filter = ('categoria',)

admin.site.register(datos, datosAdmin)


