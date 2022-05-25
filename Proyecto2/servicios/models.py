from mailbox import NoSuchMailboxError
from tabnanny import verbose
from django.db import models

# Create your models here.
class Servicio(models.Model):
    titulo = models.CharField(max_length=50) 
    contenido = models.CharField(max_length=50) 
    imagen = models.ImageField()
    created =  models.DateField(auto_now_add=True) 
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    
    def __str__(self):
        return self.titulo
