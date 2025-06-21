import re
from django import forms
from django.forms import ModelForm

from applications.core.models import Doctor, Paciente
from applications.doctor.models import AtencionMedica

class AtencionMedicaForm(ModelForm):
    class Meta:
        model = AtencionMedica
        fields = [
            "fecha",
            "hora",
            "paciente",
            "doctor",
            "motivo_consulta",
        ]
        widgets = {
            "fecha": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),
            "hora": forms.TimeInput(attrs={
                "type": "time",
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
            "motivo_consulta": forms.Textarea(attrs={
                "placeholder": "Ingrese motivo de consulta",
                "class": "form-control"
            }),
        }
        error_messages = {
            "fecha": {
                "required": "La fecha de atención es requerida.",
            },
            "hora": {
                "required": "La hora de atención es requerida.",
            },
            "paciente": {
                "required": "El nombre del paciente es requerido.",
            },
            "doctor": {
                "required": "El nombre del doctor es requerido.",
            },
        }
        
        labels = {
            "fecha": "Fecha de Atención",
            "hora": "Hora de Atención",
            "paciente": "Paciente",
            "doctor": "Doctor",
            "motivo_consulta": "Motivo de Consulta",
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configurar querysets para los selects
        self.fields['paciente'].queryset = Paciente.objects.all().order_by('apellidos', 'nombres')
        self.fields['doctor'].queryset = Doctor.objects.all().order_by('apellidos', 'nombres')
        
        # Hacer que los campos sean obligatorios
        self.fields['paciente'].empty_label = "Seleccione un paciente"
        self.fields['doctor'].empty_label = "Seleccione un doctor"
    
    
    def clean_fecha(self):
        fecha = self.cleaned_data.get("fecha")
        if not fecha:
            raise forms.ValidationError("La fecha de atención es requerida.")
        return fecha
    def clean_hora(self):
        hora = self.cleaned_data.get("hora")
        if not hora:
            raise forms.ValidationError("La hora de atención es requerida.")
        return hora
    def clean_paciente(self):
        paciente = self.cleaned_data.get("paciente")
        if not paciente:
            raise forms.ValidationError("El nombre del paciente es requerido.")
        return paciente
    
    def clean_doctor(self):
        doctor = self.cleaned_data.get("doctor")
        if not doctor:
            raise forms.ValidationError("El nombre del doctor es requerido.")
        return doctor
    def clean_motivo_consulta(self):
        motivo_consulta = self.cleaned_data.get("motivo_consulta")
        if not motivo_consulta:
            raise forms.ValidationError("El motivo de consulta es requerido.")
        return motivo_consulta
    