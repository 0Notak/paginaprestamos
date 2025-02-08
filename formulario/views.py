from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import Formulario
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import post

def enviar_email(nombre, rfc, correo, telefono):
    """
    Envía un correo electrónico con los datos proporcionados.
    """
    asunto = f"Inicio de tramite de credito de {nombre}"
    mensaje = f"Hola {nombre} estamos iniciando tu tramite de credito nos contactaremos contigo via Whatsapp al numero {telefono} o te llamaremos al numero {telefono}, recuerda contestar nuestra llamada"
    remitente = "cnominacredito@gmail.com"  # Mismo correo configurado en settings
    destinatario = [correo]

    # Enviar correo
    send_mail(asunto, mensaje, remitente, destinatario,fail_silently=False,)


@login_required
def lista_formularios(request):
    if request.method == 'POST':
        registros_marcados = request.POST.getlist('hechos')

        for formulario in Formulario.objects.all():
            formulario.hecho = str(formulario.id) in registros_marcados
            formulario.save()

        return redirect('lista_formularios')

    formularios = Formulario.objects.order_by('-id')
    
    paginator = Paginator(formularios, 25)  
    page_number = request.GET.get('page')  # Obtener el número de página desde los parámetros GET
    page_obj = paginator.get_page(page_number)
    return render(request, 'lista_formularios.html', {'registros': page_obj})


def formulario_vista(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        rfc = request.POST["rfc"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]
        dependencia = request.POST["dependencia"]
        estado = request.POST["estado"]
        rango_valor = request.POST["rango_valor"]
        
        

        # Guardar en base de datos
        Formulario.objects.create(
            nombre=nombre,
            rfc=rfc,
            correo=correo,
            telefono=telefono,
            dependencia=dependencia,
            estado=estado,
            rango_valor=rango_valor,
            
        )

        # Enviar correo
        enviar_email(nombre, rfc, correo, telefono)

        # Generar enlace de WhatsApp
        mensaje = f"Hola, soy {nombre}. Mi RFC es {rfc}. Mi correo es {correo} y mi teléfono es {telefono} Y me gustaria acelerar el tramite de mi prestamo."
        numero_whatsapp = "529518592671"  # Cambiar a tu número de WhatsApp
        enlace_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensaje.replace(' ', '%20')}"  # Formato URL

        return render(request, "formulario_exito.html", {"whatsapp_link": enlace_whatsapp})

    return render(request, "registro_formulario.html")



def blog(request, ):
    datos= post.objects.all().order_by('-localizacion_id')
    
    
    baner1=post.objects.filter(localizacion=2).values()
    baner2=post.objects.filter(localizacion=3).values()
    baner3=post.objects.filter(localizacion=4).values()
    
    
    
    paginator = Paginator(datos, 10)  # Show 25 contacts per page.
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    
    print(baner3)
    return render(request, 'blog.html', {
        "posts":posts,
        
        "banerderecha":baner1,
        "banerderechaabajo":baner2,
        "banerabajo":baner3
        })

def preview(request ,slug):
    
    posts=get_object_or_404(post, slug=slug)
    
    baner1=post.objects.filter(localizacion=2).values()
    baner2=post.objects.filter(localizacion=3).values()
    baner3=post.objects.filter(localizacion=4).values()
    
   
    
    tit=posts.titulo
    contenido=posts.contenido
    return render(request, 'preview.html', {
        "titulo":tit,
        "contenido":contenido,
        
        "banerderecha":baner1,
        "banerderechaabajo":baner2,
        "banerabajo":baner3
        
        
        
        })