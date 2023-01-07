from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=32)
    apellido = models.CharField(max_length=32)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    # al setear null y blank a true, permite que se guarden valores vacios un db relacional

    def __str__(self):
        return f"{self.name}, {self.apellido}"

# peliculas


class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    year = models.PositiveBigIntegerField()
    duration = models.PositiveBigIntegerField()
    # ForeignKey relaciona a la prop director con la clase Director

    def __str__(self):
        return f"{self.name}, {self.description}"
