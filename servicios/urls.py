from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.servicios, name="Servicios"),
    path('juego_unity/', views.juego_unity, name="Juego_unity"),
    #path('juegos/<int:juego_id>/', views.juego, name="juego"),
    
    # ------------------------------ GRÁFICAS ------------------------------
    path('grafica2/', views.grafica2, name="Grafica2"),
]

