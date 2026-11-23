from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/crear/', views.crear_empleado, name='crear_empleado'),
    path('departamentos/', views.lista_departamentos, name='lista_departamentos'),
    path('departamentos/crear/', views.crear_departamento, name='crear_departamento'),
]