from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre