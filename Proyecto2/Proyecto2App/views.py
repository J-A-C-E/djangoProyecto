from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

# Create your views here.

def inicio(request):
    return render(request, "Proyecto2App/inicio.html")

def noticia(request):
    return render(request, "Proyecto2App/noticias.html")

def servicio(request):
    servicios = Servicio.objects.all()
    return render(request, "Proyecto2App/servicios.html", {"servicios": servicios})

def contacto(request):
    return render(request, "Proyecto2App/contacto.html")
    
