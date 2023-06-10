from django.urls import path
#from . import views
from . views import VRegistro, cerrar_sesion, logear

#from blog.views import categoria


urlpatterns = [

    #path('', views.autenticacion, name = "Autenticacion"),
    path('', VRegistro.as_view(), name = "Autenticacion"),

    path('cerrar_sesion', cerrar_sesion, name = "cerrar_sesion"),

    path('logear', logear, name = "logear"),


]