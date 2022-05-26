from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "Proyecto2App/inicio.html")

def noticia(request):
    return render(request, "Proyecto2App/noticias.html")


def contacto(request):
    return render(request, "Proyecto2App/contacto.html")
    
