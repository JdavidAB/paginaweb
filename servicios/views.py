from django.shortcuts import render

from servicios.models import Servicio, Reto

from json import loads, dumps

from autenticacion.views import logear

# Create your views here.

def servicios(request):

    servicios = Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios":servicios})
    #return HttpResponse("Servicios")

#def juego(request, juego_id):

#    juego = Servicio.objects.get(id=juego_id)
#    servicios = Servicio.objects.filter(juegos=juego)
#    return render(request, "juegos/juegos.html", {'juego':juego, "servicios":servicios})

def juego_unity(request):
    return render(request, "servicios/juegos.html")


def grafica2(request):

    reto = Reto.objects.all()
    data = [['Nombre', 'Minutos jugados']]

    resultados = Reto.objects.all()

    for i in resultados:
        x = i.id_de_usuario_id #i.id_de_usuario_id
        y = i.minutos_jugados
        data.append([x, y])

    datos_formato = dumps(data)
    titulo = 'Indicador STEM'
    subtitulo = 'Minutos jugados'

    titulo_formato = dumps(titulo)
    subtitulo_formato = dumps(subtitulo)
    return render(request, "graficas/grafica2.html", {'losDatos': datos_formato, 'titulo': titulo_formato, 'subtitulo': subtitulo_formato, "reto":reto})




