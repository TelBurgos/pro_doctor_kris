import re
from django import forms
from django.forms import ModelForm

from applications.core.models import Doctor
from applications.doctor.models import HorariosAtencion

class HorariosAtencionForm(ModelForm):
    class Meta:
        model = HorariosAtencion
        fields = [
            "dia_semana",
            "hora_inicio",
            "hora_fin",
            "doctor",
        ]
        widgets = {
            "dia_semana": forms.Select(attrs={
                "class": "form-control"
            }),
            "hora_inicio": forms.TimeInput(attrs={
                "type": "time",
                "class": "form-control"
            }),
            "hora_fin": forms.TimeInput(attrs={
                "type": "time",
                "class": "form-control"
            }),
            "doctor": forms.Select(attrs={
                "class": "form-control"
            }),
        }
        error_messages = {
            "dia_semana": {
                "required": "El día de la semana es requerido.",
            },
            "hora_inicio": {
                "required": "La hora de inicio es requerida.",
            },
            "hora_fin": {
                "required": "La hora de fin es requerida.",
            },
            "doctor": forms.Select(attrs={
                "class": "form-control",
                "data-placeholder": "Seleccione un doctor"
            }),
        }
        labels = {
            "dia_semana": "Día de la Semana",
            "hora_inicio": "Hora de Inicio",
            "hora_fin": "Hora de Fin",
            "doctor": "Doctor",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configurar querysets para los selects
        self.fields['doctor'].queryset = Doctor.objects.all().order_by('apellidos', 'nombres')
        
        # Hacer que los campos sean obligatorios
        self.fields['doctor'].empty_label = "Seleccione un doctor"
    
    def clean_hora_fin(self):
        hora_inicio = self.cleaned_data.get('hora_inicio')
        hora_fin = self.cleaned_data.get('hora_fin')
        if hora_inicio and hora_fin and hora_fin <= hora_inicio:
            raise forms.ValidationError("La hora de fin debe ser posterior a la hora de inicio.")
        return hora_fin
    def clean_hora_inicio(self):
        hora_inicio = self.cleaned_data.get('hora_inicio')
        if not hora_inicio:
            raise forms.ValidationError("La hora de inicio es requerida.")
        return hora_inicio
    def clean_dia_semana(self):
        dia_semana = self.cleaned_data.get('dia_semana')
        if not dia_semana:
            raise forms.ValidationError("El día de la semana es requerido.")
        return dia_semana
    def clean_doctor(self):
        doctor = self.cleaned_data.get('doctor')
        if not doctor:
            raise forms.ValidationError("El doctor es requerido.")
        return doctor
    
