from django.db import models

class Especie(models.Model):
    idEspecie = models.IntegerField(primary_key=True, verbose_name='Id de especie')
    nombreEspecie = models.CharField(max_length=50, verbose_name='Nombre de la especie')

    def str(self):
        return self.nombreEspecie

class Animal(models.Model):
    numChip = models.CharField(max_length=20, primary_key=True, verbose_name='Numero de chip')
    nombreAnimal = models.CharField(max_length=50, verbose_name='Nombre animal')
    edadAnimal = models.IntegerField(verbose_name='Edad animal')
    generoAnimal = models.CharField(max_length=6, verbose_name='Género animal')
    esterilizado = models.BooleanField(verbose_name='Esterilizado')
    fotografia = models.ImageField(blank = True, verbose_name = 'Fotografía animal')
    especie =models.ForeignKey(Especie, on_delete=models.CASCADE)
    def str(self):
        return self.nombreAnimal