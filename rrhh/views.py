from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Empleado, Departamento, Cargo, Contrato, Asistencia
from .forms import EmpleadoForm, DepartamentoForm, CargoForm, ContratoForm, AsistenciaForm

def home(request):
    return render(request, 'home.html')

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista.html', {'empleados': empleados})

def crear_empleado(request):
    form = EmpleadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_empleados')
    return render(request, 'empleados/crear.html', {'form': form})

def lista_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos/lista.html', {'departamentos': departamentos})

def crear_departamento(request):
    form = DepartamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_departamentos')
    return render(request, 'departamentos/crear.html', {'form': form})


# Contratos Views
@login_required(login_url='login')
def listar_contratos(request):
    contratos = Contrato.objects.filter(estado=True)
    return render(request, 'rrhh/contratos/listar.html', {'contratos': contratos})

@login_required(login_url='login')
def crear_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro creado correctamente.")
            return redirect('listar_contratos')
        messages.error(request, "Error en el formulario.")
    else:
        form = ContratoForm()
    return render(request, 'rrhh/contratos/formulario.html', {'form': form, 'accion': 'Crear'})

@login_required(login_url='login')
def editar_contrato(request, id):
    contrato = Contrato.objects.filter(id=id, estado=True).first()
    if not contrato:
        messages.error(request, "Registro no encontrado.")
        return redirect('listar_contratos')

    if request.method == 'POST':
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro actualizado correctamente.")
            return redirect('listar_contratos')
        messages.error(request, "Error en el formulario.")
    else:
        form = ContratoForm(instance=contrato)
    return render(request, 'rrhh/contratos/formulario.html', {'form': form, 'accion': 'Editar'})

@login_required(login_url='login')
def eliminar_contrato(request, id):
    contrato = Contrato.objects.filter(id=id, estado=True).first()
    if not contrato:
        messages.error(request, "Registro no encontrado.")
    else:
        contrato.estado = False  # Eliminado lógico
        contrato.save()
        messages.success(request, "Registro eliminado correctamente.")
    return redirect('listar_contratos')

#asistencia views
@login_required(login_url='login')
def listar_asistencias(request):
    asistencias = Asistencia.objects.filter(estado=True)
    return render(request, 'rrhh/asistencias/listar.html', {'asistencias': asistencias})

@login_required(login_url='login')
def crear_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro creado correctamente.")
            return redirect('listar_asistencias')
        messages.error(request, "Error en el formulario.")
    else:
        form = AsistenciaForm()
    return render(request, 'rrhh/asistencias/formulario.html', {'form': form, 'accion': 'Crear'})

@login_required(login_url='login')
def editar_asistencia(request, id):
    asistencia = Asistencia.objects.filter(id=id, estado=True).first()
    if not asistencia:
        messages.error(request, "Registro no encontrado.")
        return redirect('listar_asistencias')

    if request.method == 'POST':
        form = AsistenciaForm(request.POST, instance=asistencia)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro actualizado correctamente.")
            return redirect('listar_asistencias')
        messages.error(request, "Error en el formulario.")
    else:
        form = AsistenciaForm(instance=asistencia)
    return render(request, 'rrhh/asistencias/formulario.html', {'form': form, 'accion': 'Editar'})

@login_required(login_url='login')
def eliminar_asistencia(request, id):
    asistencia = Asistencia.objects.filter(id=id, estado=True).first()
    if not asistencia:
        messages.error(request, "Registro no encontrado.")
    else:
        asistencia.estado = False  # Eliminado lógico
        asistencia.save()
        messages.success(request, "Registro eliminado correctamente.")
    return redirect('listar_asistencias')