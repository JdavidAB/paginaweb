from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from django.contrib import messages
from pedidos.models import LineaPedido, Pedido
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url = "/autenticacion/logear")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user = request.user)
    carro = Carro(request)
    lineas_pedido = list()

    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(

            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido

        ))

    # me permite almacenar la lista de pedidos en la base de datos
    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(pedido = pedido,
                lineas_pedido = lineas_pedido,
                nombreusuario = request.user.username,
                emailusuario = request.user.email)

    messages.success(request, "El pedido se ha creado correctamente")

    return redirect("../tablas")

def enviar_mail(**kwargs):

    asunto = "Gracias por el pedido"
    mensaje = render_to_string("emails/pedido.html",{

        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario": kwargs.get("nombreusuario")

    })

    mensaje_texto = strip_tags(mensaje)
    from_email = "david.aguilarbetancourth@gmail.com"   # es el Correo de la tienda
    to = kwargs.get("emailusuario")  # A quien va el correo

    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)

