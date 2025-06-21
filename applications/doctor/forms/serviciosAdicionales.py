import re
from django import forms
from django.forms import ModelForm

from applications.doctor.models import ServiciosAdicionales

class ServiciosAdicionalesForm(ModelForm):
    class Meta:
        model = ServiciosAdicionales
        fields = [
            "fecha_servicio",
            "tipo_servicio",
            "paciente",
            "doctor",
            "descripcion",
        ]
        widgets = {
            "fecha_servicio": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),
            "tipo_servicio": forms.TextInput(attrs={
                "placeholder": "Ingrese tipo de servicio",
                "class": "form-control"
            }),
            "paciente": forms.TextInput(attrs={
                "placeholder": "Ingrese nombre del paciente",
                "class": "form-control"
            }),
            "doctor": forms.TextInput(attrs={
                "placeholder": "Ingrese nombre del doctor",
                "class": "form-control"
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Ingrese descripción del servicio",
                "class": "form-control"
            }),
        }
        error_messages = {
            "fecha_servicio": {
                "required": "La fecha del servicio es requerida.",
            },
            "tipo_servicio": {
                "required": "El tipo de servicio es requerido.",
            },
            "paciente": {
                "required": "El nombre del paciente es requerido.",
            },
            "doctor": {
                "required": "El nombre del doctor es requerido.",
            },
        }
        labels = {
            "fecha_servicio": "Fecha del Servicio",
            "tipo_servicio": "Tipo de Servicio",
            "paciente": "Paciente",
            "doctor": "Doctor",
            "descripcion": "Descripción del Servicio",
        }

    def clean_fecha_servicio(self):
        fecha_servicio = self.cleaned_data.get('fecha_servicio')
        if not fecha_servicio:
            raise forms.ValidationError("La fecha del servicio es requerida.")
        return fecha_servicio
    def clean_tipo_servicio(self):
        tipo_servicio = self.cleaned_data.get('tipo_servicio')
        if not tipo_servicio:
            raise forms.ValidationError("El tipo de servicio es requerido.")
        if not re.match(r'^[a-zA-Z\s]+$', tipo_servicio):
            raise forms.ValidationError("El tipo de servicio solo puede contener letras y espacios.")
        return tipo_servicio
    def clean_paciente(self):
        paciente = self.cleaned_data.get('paciente')
        if not paciente:
            raise forms.ValidationError("El nombre del paciente es requerido.")
        if not re.match(r'^[a-zA-Z\s]+$', paciente):
            raise forms.ValidationError("El nombre del paciente solo puede contener letras y espacios.")
        return paciente
    def clean_doctor(self):
        doctor = self.cleaned_data.get('doctor')
        if not doctor:
            raise forms.ValidationError("El nombre del doctor es requerido.")
        if not re.match(r'^[a-zA-Z\s]+$', doctor):
            raise forms.ValidationError("El nombre del doctor solo puede contener letras y espacios.")
        return doctor
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if not descripcion:
            raise forms.ValidationError("La descripción del servicio es requerida.")
        if len(descripcion) < 10:
            raise forms.ValidationError("La descripción debe tener al menos 10 caracteres.")
        return descripcion
    
