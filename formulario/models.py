from django.db import models



class Formulario(models.Model):
    nombre = models.CharField(max_length=30)
    rfc = models.CharField(max_length=13)
    correo = models.EmailField()
    estado = models.CharField(max_length=15)
    dependencia = models.CharField(max_length=15)
    rango_valor = models.IntegerField(default=0)
    telefono = models.CharField(max_length=10)
    hecho = models.BooleanField(default=False)  # Para el checklist

    def __str__(self):
        return self.nombre

class localizacion(models.Model):
    categorias = models.CharField(max_length=80)
    def __str__(self):
        return self.categorias 


class post(models.Model):
    titulo = models.CharField(max_length=80,unique=True,primary_key=True, help_text='Titulo del post')
    contenido = models.CharField(max_length=4000)
    localizacion = models.ForeignKey(localizacion, on_delete=models.PROTECT)
    fecha = models.DateField(auto_now_add="True")
    miniatura = models.ImageField( blank=True)
    slug = models.SlugField()
    def __str__(self):
        return self.titulo 