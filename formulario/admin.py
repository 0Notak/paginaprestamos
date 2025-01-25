from django.contrib import admin
from .models import post, localizacion
from django_summernote.admin import SummernoteModelAdmin


class Summernote(SummernoteModelAdmin):
    summernote_fields = ('contenido')
    
# Register your models here.
admin.site.register(localizacion,)
admin.site.register(post, Summernote)