from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    presupuesto = models.IntegerField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Arriendo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    valor = models.IntegerField()

    def __str__(self):
        return self.nombre
