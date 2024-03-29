# Generated by Django 5.0 on 2024-01-26 18:23

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
                ('description', models.CharField(max_length=255, verbose_name='descripcion')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='titulo')),
                ('content', ckeditor.fields.RichTextField(verbose_name='contenido')),
                ('imagen', models.ImageField(default='null', upload_to='', verbose_name='imagen')),
                ('public', models.BooleanField(verbose_name='publicado')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha_creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='fecha_modificacion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
                ('categories', models.ManyToManyField(blank=True, null=True, to='blog.category', verbose_name='categorias')),
            ],
            options={
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
            },
        ),
    ]
