from django.urls import path
from Proyecto2App import views

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('servicios',views.servicio, name="Servicios"),
    path('noticias',views.noticia, name="Noticias"),
    path('contacto',views.contacto, name="Contacto")
]