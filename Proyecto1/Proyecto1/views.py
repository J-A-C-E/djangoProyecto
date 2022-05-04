from datetime import datetime
from django.http import HttpResponse
import datetime

def saludo(request):
    documento="<html><body><h1>Primera pagina con Django</h1></body></html>"

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
