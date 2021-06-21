from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home, index, nosotros, donaciones, perro, gato, contacto

urlpatterns = [
    path('', index, name = "index"),
    path('nosotros', nosotros, name = "nosotros"),
    path('contacto', contacto, name = "contacto"),
    path('perro', perro, name = "perro"),
    path('gato', gato, name = "gato"),
    path('donaciones', donaciones, name = "donaciones"),
    # path('form_vehiculo', form_vehiculo, name = "form_vehiculo"),
    # path('form_mod_vehiculo/<id>', form_mod_vehiculo, name = "form_mod_vehiculo"),
    # path('form_del_vehiculo/<id>', form_del_vehiculo, name = "form_del_vehiculo")
]
