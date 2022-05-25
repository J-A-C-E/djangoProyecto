from django.urls import path
from Proyecto2App import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('servicios',views.servicio, name="Servicios"),
    path('noticias',views.noticia, name="Noticias"),
    path('contacto',views.contacto, name="Contacto")
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)