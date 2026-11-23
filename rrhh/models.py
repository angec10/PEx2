from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    cedula = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=10, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.TextField(blank=True)

    class Meta:
        db_table = 'usuario'


class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self): return self.nombre


class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self): return self.nombre


class Empleado(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    fecha_ingreso = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"