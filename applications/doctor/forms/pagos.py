import re
from django import forms
from django.forms import ModelForm

from applications.core.models import Doctor, Paciente
from applications.doctor.models import Pagos

class PagosForm(ModelForm):
    class Meta:
        model = Pagos
        fields = [
            "fecha_pago",
            "monto",
            "paciente",
            "doctor",
            "descripcion",
        ]
        widgets = {
            "fecha_pago": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),
            "monto": forms.NumberInput(attrs={
                "placeholder": "Ingrese monto del pago",
                "class": "form-control"
            }),
            "paciente": forms.Select(attrs={
                "class": "form-control",
                "data-placeholder": "Seleccione un paciente"
            }),
            "doctor": forms.Select(attrs={
                "class": "form-control",
                "data-placeholder": "Seleccione un doctor"
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Ingrese descripción del pago",
                "class": "form-control"
            }),
        }
        error_messages = {
            "fecha_pago": {
                "required": "La fecha de pago es requerida.",
            },
            "monto": {
                "required": "El monto del pago es requerido.",
            },
            "paciente": {
                "required": "El nombre del paciente es requerido.",
            },
            "doctor": {
                "required": "El nombre del doctor es requerido.",
            },
        }
        labels = {
            "fecha_pago": "Fecha de Pago",
            "monto": "Monto del Pago",
            "paciente": "Paciente",
            "doctor": "Doctor",
            "descripcion": "Descripción del Pago",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configurar querysets para los selects
        self.fields['paciente'].queryset = Paciente.objects.all().order_by('apellidos', 'nombres')
        self.fields['doctor'].queryset = Doctor.objects.all().order_by('apellidos', 'nombres')
        
        # Hacer que los campos sean obligatorios
        self.fields['paciente'].empty_label = "Seleccione un paciente"
        self.fields['doctor'].empty_label = "Seleccione un doctor"
    
    
    def clean_fecha_pago(self):
        fecha_pago = self.cleaned_data.get('fecha_pago')
        if not fecha_pago:
            raise forms.ValidationError("La fecha de pago es requerida.")
        return fecha_pago
    def clean_monto(self):
        monto = self.cleaned_data.get('monto')
        if not monto:
            raise forms.ValidationError("El monto del pago es requerido.")
        if monto <= 0:
            raise forms.ValidationError("El monto del pago debe ser mayor a cero.")
        return monto
    def clean_paciente(self):
        paciente = self.cleaned_data.get('paciente')
        if not paciente:
            raise forms.ValidationError("El nombre del paciente es requerido.")
        if not re.match(r'^[a-zA-Z\s]+$', paciente):
            raise forms.ValidationError("El nombre del paciente solo debe contener letras y espacios.")
        return paciente
    def clean_doctor(self):
        doctor = self.cleaned_data.get('doctor')
        if not doctor:
            raise forms.ValidationError("El nombre del doctor es requerido.")
        if not re.match(r'^[a-zA-Z\s]+$', doctor):
            raise forms.ValidationError("El nombre del doctor solo debe contener letras y espacios.")
        return doctor
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if not descripcion:
            raise forms.ValidationError("La descripción del pago es requerida.")
        if len(descripcion) < 10:
            raise forms.ValidationError("La descripción del pago debe tener al menos 10 caracteres.")
        return descripcion
    