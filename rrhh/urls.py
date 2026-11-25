from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/crear/', views.crear_empleado, name='crear_empleado'),
    path('departamentos/', views.lista_departamentos, name='lista_departamentos'),
    path('departamentos/crear/', views.crear_departamento, name='crear_departamento'),
    path('contratos/', views.listar_contratos, name='listar_contratos'),
    path('contratos/crear/', views.crear_contrato, name='crear_contrato'),
    path('contratos/editar/<int:id>/', views.editar_contrato, name='editar_contrato'),
    path('contratos/eliminar/<int:id>/', views.eliminar_contrato, name='eliminar_contrato'),
    path('asistencias/', views.listar_asistencias, name='listar_asistencias'),
    path('asistencias/crear/', views.crear_asistencia, name='crear_asistencia'),
    path('asistencias/editar/<int:id>/', views.editar_asistencia, name='editar_asistencia'),
    path('asistencias/eliminar/<int:id>/', views.eliminar_asistencia, name='eliminar_asistencia'),
]