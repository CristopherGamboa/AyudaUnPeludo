from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalForm


# Create your views here.

def animals_list(request):
    animales = Animal.objects.all()
    datos = {
        'animales': animales
    }
    return render(request, 'core/animals_list.html', datos)

def index(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def gato(request):
    animales = Animal.objects.all()
    datos = {
        'animales': animales
    }
    return render(request, 'core/gato.html', datos)

def perro(request):
    animales = Animal.objects.all()
    datos = {
        'animales': animales
    }
    return render(request, 'core/perro.html', datos)

def contacto(request):
    return render(request, 'core/contacto.html')

def donaciones(request):
    return render(request, 'core/donaciones.html')

def fichaAnimal(request, id):
    animal = Animal.objects.get(nombreAnimal = id)

    datos= {
        'an': animal
    }
    return render(request, 'core/fichaAnimal.html', datos)

def form_animal(request):

    datos= {
        'form': AnimalForm()
    }

    if request.method == 'POST':
        formulario = AnimalForm(request.POST, request.FILES)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente."
        else:
            datos['mensaje'] = "Se ha producido un error."

    return render(request, 'core/form_animal.html', datos)

def form_mod_animal(request, id):

    animal = Animal.objects.get(nombreAnimal = id)

    datos= {

        'form': AnimalForm(instance=animal)

    }

    if request.method == 'POST':

        formulario = AnimalForm(request.POST, request.FILES, instance= animal)

        if formulario.is_valid:

            formulario.save()

            datos['mensaje'] = "Datos guardados correctamente"
        else:
            datos['mensaje'] = "Se ha producido un error."



    return render(request, 'core/form_mod_animal.html', datos)

def form_del_animal(request, id):

    animal = Animal.objects.get(nombreAnimal = id)

    animal.delete()

    return redirect(to='animals_list')