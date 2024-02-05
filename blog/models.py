from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='nombre')
    description = models.CharField(max_length=255, verbose_name='descripcion')
    created_at =models.DateField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateField(auto_now=True, verbose_name='Actualizado el')

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='titulo')
    content = RichTextField(verbose_name='contenido')
    imagen = models.ImageField(default='null', verbose_name='imagen', upload_to="articles")
    public = models.BooleanField( verbose_name='publicado')
    user = models.ForeignKey(User, verbose_name = 'usuario', editable= False, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='categorias', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='fecha_creacion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='fecha_modificacion')

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['-create_at']

    def __str__(self):
        return self.title
