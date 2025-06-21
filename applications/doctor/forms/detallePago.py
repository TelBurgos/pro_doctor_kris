import re
from django import forms
from django.forms import ModelForm

from applications.doctor.models import DetallePago

class DetallePagoForm(ModelForm):
    class Meta:
        model = DetallePago
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
            "paciente": forms.TextInput(attrs={
                "placeholder": "Ingrese nombre del paciente",
                "class": "form-control"
            }),
            "doctor": forms.TextInput(attrs={
                "placeholder": "Ingrese nombre del doctor",
                "class": "form-control"
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
    def clean_fecha_pago(self):
        fecha_pago = self.cleaned_data.get('fecha_pago')
        if not fecha_pago:
            raise forms.ValidationError("La fecha de pago es requerida.")
        return fecha_pago
    def clean_monto(self):
        monto = self.cleaned_data.get('monto')
        if not monto:
            raise forms.ValidationError("El monto del pago es requerido.")
        if not re.match(r'^\d+(\.\d{1,2})?$', str(monto)):
            raise forms.ValidationError("El monto debe ser un número válido con hasta dos decimales.")
        return monto
    
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
            raise forms.ValidationError("La descripción del pago es requerida.")
        if len(descripcion) < 10:
            raise forms.ValidationError("La descripción debe tener al menos 10 caracteres.")
        return descripcion
    