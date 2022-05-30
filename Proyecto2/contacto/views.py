from django.shortcuts import render
from . forms import FormularioContacto

# Create your views here.
def contacto(request):
    fomrulacio_contacto = FormularioContacto()
    return render(request, "contacto/contacto.html", {'miFormulario': FormularioContacto})
    