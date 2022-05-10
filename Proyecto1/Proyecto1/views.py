from datetime import datetime
from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
def saludo(request): #Primera vista
    p1 = Persona("Javier","Cruz")

    nombre = "Juan"
    apellido = "Diaz"
    ahora = datetime.datetime.now()

    doc_externo = open("C:/Users/JACE/OneDrive - Instituto Tecnológico de Nuevo Laredo/10 Semestre/Django/Proyecto1/Proyecto1/plantillas/miPlantilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido, "momento_actual":ahora})
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
