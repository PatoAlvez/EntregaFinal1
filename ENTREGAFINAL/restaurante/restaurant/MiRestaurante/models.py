from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entrada(models.Model):
    plato=models.CharField(max_length=40)
    cantidad=models.IntegerField(default= 1)
    bebida=models.CharField(max_length=40)
    numero_de_mesa=models.CharField(max_length=5)
    imagen=models.ImageField(default= "/imagenes")
    blank=True

    def __str__(self):
        return f"Plato:{self.plato}- Bebida: {self.bebida}- Numero de Mesa: {self.numero_de_mesa}"
        
class PlatoPrincipal(models.Model):
    plato=models.CharField(max_length=40)
    cantidad=models.IntegerField(default= 1)
    bebida=models.CharField(max_length=40)
    numero_de_mesa=models.CharField(max_length=5)
    imagen=models.ImageField(default="/imagenes")
    blank=True

    def __str__(self):
        return f"Plato:{self.plato} - Cantidad: {self.cantidad}- Bebida: {self.bebida}- Numero de Mesa: {self.numero_de_mesa}"

class Postre(models.Model):
    postres=models.CharField(max_length=40)
    cantidad=models.IntegerField(default= 1)
    numero_de_mesa=models.CharField(max_length=5)
    imagen=models.ImageField(default="/imagenes")
    blank=True

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="avatares", null=True, blank=True)
    blank=True

    def __str__(self):
        return f"{self.user} - {self.imagen}"
