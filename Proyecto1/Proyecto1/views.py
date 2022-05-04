from datetime import datetime
from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request): #Primera vista
    doc_externo = open("C:/Users/JACE/OneDrive - Instituto Tecnológico de Nuevo Laredo/10 Semestre/Django/Proyecto1/Proyecto1/plantillas/miPlantilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="<html><body><h1>Fecha y hora actuales %s</h1></body></html>" % fecha_actual
    return HttpResponse(documento)

def calcularEdad(request,edad,agno):
    #edadActual = 23
    periodo = agno - 2022
    edadFutura = edad + periodo
    documento="<html><body><h1>En el año %s tendrás %s años</h1></body></html>" % (agno,edadFutura)
    return HttpResponse(documento)
