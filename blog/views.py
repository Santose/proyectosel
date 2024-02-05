from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='index')
def list(request):
    # obtener articulos
    articles = Article.objects.all()
    # Paginar os articulos
    paginator = Paginator(articles,2)
    # recoer el nº de pagina
    page= request.GET.get('page')
    # paginar todos los articulos en page_articles
    page_articles = paginator.get_page(page)


    return render(request,'articles/list.html', {
        'title': 'Articulos',
        #'articles': articles
        'articles': page_articles
    })

@login_required(login_url='index')
def category(request, category_id):
    
    #category = Category.objects.get(id=category_id)
    # Pagina de error 404 error si no existe la categoria y si existe devuelve la categoria
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(categories=category_id)

    return render(request, 'categories/category.html', {
        'category': category
        #'articles': articles
    })

@login_required(login_url='index')
def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail.html', {
        'article': article

    })