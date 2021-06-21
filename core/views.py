from django.shortcuts import render
from .models import Animal
from core.forms import AnimalForm

# Create your views here.

def home(request):
    animales = Animal.objects.all()
    datos = {
        'animales': animales
    }
    return render(request, 'core/home.html', datos)

def index(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def gato(request):
    return render(request, 'core/gato.html')

def perro(request):
    return render(request, 'core/perro.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def donaciones(request):
    return render(request, 'core/donaciones.html')

def form_animal(request):

    datos= {
        'form': AnimalForm()
    }

    if request.method == 'POST':

        formulario = AnimalForm(request.POST)

        if formulario.is_valid:

            formulario.save()

            datos['mensaje'] = "Datos guardados correctamente."

    return render(request, 'core/form_animal.html', datos)

# def form_mod_vehiculo(request, id):

#     vehiculo = Vehiculo.objects.get(patente = id)

#     datos= {

#         'form': VehiculoForm(instance=vehiculo)

#     }



#     if request.method == 'POST':

#         formulario = VehiculoForm(data = request.POST, instance=vehiculo)



#         if formulario.is_valid:

#             formulario.save()



#             datos['mensaje'] = "Datos guardados correctamente"



#     return render(request, 'core/form_mod_vehiculo.html', datos)

# def form_del_vehiculo(request, id):

#     vehiculo = Vehiculo.objects.get(patente = id)

#     vehiculo.delete()

#     return redirect(to='home')