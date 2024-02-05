
from blog.models import Category,Article

def get_categories(request):
    #obtenemos los ids de los articulos
    ids = Article.objects.filter(public=True).values_list('categories',flat=True)
    # esto es una subconsultas(id__in=ids) para sacar las categorias que tienen articulos
    categories = Category.objects.filter(id__in=ids).values_list('id','name')
    return {
        'categories': categories
    }
