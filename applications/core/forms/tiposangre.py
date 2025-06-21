from django import forms
from django.forms import ModelForm
from applications.core.models import TipoSangre

class TipoSangreForm(ModelForm):
    class Meta:
        model = TipoSangre
        fields = ["tipo"]

        error_messages = {
            "tipo": {
                "unique": "Este tipo de sangre ya está registrado.",
                "required": "El tipo de sangre es obligatorio.",
            },
        }

        widgets = {
            "tipo": forms.TextInput(attrs={
                "placeholder": "Ej. A+, O-, AB-",
                "id": "id_tipo",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 "
                         "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 "
                         "dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
        }

        labels = {
            "tipo": "Tipo de Sangre",
        }

    def clean_tipo(self):
        return self.cleaned_data.get("tipo").upper()
