from django.urls import path
from . import views

urlpatterns = [
    path('',views.noticia, name="Noticias"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
]
