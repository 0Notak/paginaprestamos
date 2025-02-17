# Generated by Django 4.2.1 on 2025-01-21 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('rfc', models.CharField(max_length=13)),
                ('correo', models.EmailField(max_length=254)),
                ('estado', models.CharField(max_length=15)),
                ('dependencia', models.CharField(max_length=15)),
                ('rango_valor', models.IntegerField(default=0)),
                ('telefono', models.CharField(max_length=10)),
                ('hecho', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='localizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorias', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('titulo', models.CharField(help_text='Titulo del post', max_length=80, primary_key=True, serialize=False, unique=True)),
                ('contenido', models.CharField(max_length=4000)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('miniatura', models.ImageField(blank=True, upload_to='')),
                ('slug', models.SlugField()),
                ('localizacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='formulario.localizacion')),
            ],
        ),
    ]
