from django.shortcuts import render
from noticia.models import Post

# Create your views here.
def noticia(request):
    posts = Post.objects.all()
    return render(request, "noticia/noticias.html", {"posts": posts})
