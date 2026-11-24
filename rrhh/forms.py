from django import forms
from django.core.exceptions import ValidationError
from .models import Empleado, Departamento, Cargo, Contrato, Asistencia

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['usuario', 'departamento', 'cargo', 'activo']

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre']

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre']


class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        exclude = ['estado']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        datos = super().clean()
        inicio = datos.get('fecha_inicio')
        fin = datos.get('fecha_fin')

        if inicio and fin and fin < inicio:
            raise ValidationError("La fecha de finalización no puede ser anterior a la de inicio.")
        return datos
 

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        exclude = ['estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_entrada': forms.TimeInput(attrs={'type': 'time'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        datos = super().clean()
        entrada, salida = datos.get('hora_entrada'), datos.get('hora_salida')
        empleado, fecha = datos.get('empleado'), datos.get('fecha')

        if entrada and salida and salida <= entrada:
            raise ValidationError("La hora de salida debe ser posterior a la de entrada.")
        if not self.instance.pk and Asistencia.objects.filter(empleado=empleado, fecha=fecha, estado=True).exists():
            raise ValidationError("Ya existe asistencia para este empleado en esa fecha.")
        return datos