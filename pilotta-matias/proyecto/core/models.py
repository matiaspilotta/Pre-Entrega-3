from django.db import models

# Create your models here.

class Pais(models.Model):
    pais = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.pais}"



class identificador(models.Model):
    identificador = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.identificador}"



class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email}"


