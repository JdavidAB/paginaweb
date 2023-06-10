from django.shortcuts import render, redirect

from django.views.generic import View

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, logout, authenticate

from django.contrib import messages



from servicios.models import Reto



# Create your views here.

#def autenticacion(request):
    
#    return render(request, "registro/registro.html")

class VRegistro(View):

    def get(self, request):   # renderiza el formulario
        
        form = UserCreationForm()
        return render(request, "registro/registro.html",{"form":form})

    def post(self, request):  # envia los datos a la base de datos.
        
        form = UserCreationForm(request.POST)

        if form.is_valid():
        
            usuario = form.save()

            login(request, usuario)
            
            # Crea un registro en RETO con el usuario creado
            Reto.objects.create(id_de_usuario=usuario, minutos_jugados="0", minimo="0", maximo="0", repeticion_niveles="0", engranes="0",
                                duracion_promedio="0", success_promedio="0", a_que_nivel_llego="0", sesion_iniciada_dia="0", sesion_iniciada_mes="0")
            
            #Reto.objects.create(id_de_usuario_id=request.user.id, minutos_jugados="0", minimo="0", maximo="0", repeticion_niveles="0", engranes="0",
                                #duracion_promedio="0", success_promedio="0", a_que_nivel_llego="0", sesion_iniciada_dia="0", sesion_iniciada_mes="0")
            
            #resultados = Reto.objects.filter(id_de_usuario_id=usuario)
            #minutos_info = resultados[0].minutos_jugados
            #veces_info = resultados[0].repeticion_niveles
            #engranes_info = resultados[0].engranes

            return redirect('Home')
        
        else:
            
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request, "registro/registro.html",{"form":form}) #, "engranes_info": engranes_info, "veces_info": veces_info, "minutos_info": minutos_info})
        

def cerrar_sesion(request):

    logout(request)
    return redirect('Home')


def logear(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)

                #resultados = Reto.objects.filter(id_de_usuario_id=usuario)
                #minutos_info = resultados[0].minutos_jugados
                #veces_info = resultados[0].repeticion_niveles
                #engranes_info = resultados[0].engranes

                return redirect('Home')
            
            else:
                messages.error(request, "Usuario no valido")
        
        else:
            messages.error(request, "Informacion incorrecta")  

    form = AuthenticationForm()

    return render(request, "login/login.html",{"form":form}) #, "engranes_info": engranes_info, "veces_info": veces_info, "minutos_info": minutos_info}) # }) #
