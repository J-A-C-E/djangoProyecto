from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("Inicio")

def noticia(request):
    return HttpResponse("Noticias")

def servicio(request):
    return HttpResponse("Servicios")

def contacto(request):
    return HttpResponse("Contacto")
    
