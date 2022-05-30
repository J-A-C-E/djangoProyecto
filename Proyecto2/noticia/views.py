from django.shortcuts import render
from noticia.models import Categoria, Post, Categoria

# Create your views here.
def noticia(request):
    posts = Post.objects.all()
    return render(request, "noticia/noticias.html", {"posts": posts})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id = categoria_id)
    posts = Post.objects.filter(categorias = categoria)
    return render(request, "noticia/categorias.html", {'categoria':categoria, "posts": posts})