from django.db import models

class Especie(models.Model):
    idEspecie = models.IntegerField(primary_key=True, verbose_name='Id de especie')
    nombreEspecie = models.CharField(max_length=50, verbose_name='Nombre de la especie')

    def __str__(self):
        return self.nombreEspecie

class Genero(models.Model):
    idGenero = models.IntegerField(primary_key=True, verbose_name='Id del género')
    nombreGenero = models.CharField(max_length=50, verbose_name='Nombre del género')

    def __str__(self):
        return self.nombreGenero

class Animal(models.Model):
    numChip = models.CharField(max_length=20, primary_key=True, verbose_name='Numero de chip')
    nombreAnimal = models.CharField(max_length=50, verbose_name='Nombre animal')
    edadAnimal = models.IntegerField(verbose_name='Edad animal')
    especie =models.ForeignKey(Especie, on_delete=models.CASCADE, verbose_name = 'Especie')
    generoAnimal = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name = 'Género')
    esterilizado = models.BooleanField(verbose_name='Esterilizado')
    fotografia = models.ImageField(blank = True, verbose_name = 'Fotografía animal')
    def __str__(self):
        return self.nombreAnimal