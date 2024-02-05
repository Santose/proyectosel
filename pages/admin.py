from django.contrib import admin
from .models import Page

#configuracion extra
class PageAdmin(admin.ModelAdmin):
    # campos de solo lectura
    readonly_fields = ('created_at','updated_at')
    #campos a utilizar por el buscador 
    search_fields=('title','content')
    #sacar un filtro para poder elegir (en este caso por visible)
    list_filter = ('visible',)
    #campos que debemos sacar
    list_display = ('title','order','visible','slug','created_at')
    # ordenar
    ordering = ('-created_at',)


# Register your models here.
admin.site.register(Page, PageAdmin)

# cambiar titulo y subtitulo del panel y 
title = 'Panel de paginas '
subtitle = 'subpanel de paginas '
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle