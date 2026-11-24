from django.contrib import admin
from .models import Asistencia, Contrato, Usuario, Departamento, Cargo, Empleado

admin.site.register(Usuario)
admin.site.register(Departamento)
admin.site.register(Cargo)
admin.site.register(Empleado)
admin.site.register(Contrato)
admin.site.register(Asistencia)