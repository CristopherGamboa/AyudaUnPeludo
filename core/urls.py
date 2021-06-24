from os import stat
from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from django.conf import settings
from django.conf.urls.static import static
from .views import index, nosotros, donaciones, perro, gato, contacto, form_animal, form_del_animal, form_mod_animal, animals_list, fichaAnimal

urlpatterns = [
    path('', index, name = "index"),
    path('nosotros', nosotros, name = "nosotros"),
    path('contacto', contacto, name = "contacto"),
    path('perros', perro, name = "perro"),
    path('gatos', gato, name = "gato"),
    path('donaciones', donaciones, name = "donaciones"),
    path('animals_list', animals_list, name = "animals_list"),
    path('form_animal', form_animal, name = "form_animal"),
    path('form_mod_animal/<id>', form_mod_animal, name = "form_mod_animal"),
    path('form_del_animal/<id>', form_del_animal, name = "form_del_animal"),
    path('fichaAnimal/<id>', fichaAnimal, name = "fichaAnimal")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
