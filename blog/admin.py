from django.contrib import admin
from .models import Category, Article

#configuracion extra
class CategoryAdmin(admin.ModelAdmin):
    # campos de solo lectura
    readonly_fields = ('created_at', 'updated_at')
    #campos a utilizar por el buscador 
    search_fields=('name',)
    #sacar un filtro para poder elegir (en este caso por visible)
    list_filter = ('name',)
    #campos que debemos sacar
    list_display = ('name','created_at')
    # ordenar
    ordering = ('-created_at',)

class ArticleAdmin(admin.ModelAdmin):
    # campos de solo lectura
    readonly_fields = ('create_at', 'updated_at')
    #campos a utilizar por el buscador 
    search_fields=('title','public','user')
    #sacar un filtro para poder elegir (en este caso por visible)
    list_filter = ('public',)
    #campos que debemos sacar
    list_display = ('title','public','user','create_at')
    # ordenar
    ordering = ('-create_at',)

    def save_model(selt, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
