from django.urls import path
from applications.doctor.views.atencionMedica import (AtencionMedicaCreateView,AtencionMedicaDeleteView,AtencionMedicaListView,AtencionMedicaUpdateView)


app_name = 'doctor'

urlpatterns = [
    path('atencion_medica/', AtencionMedicaListView.as_view(), name='atencion_medica_list'),
    path('atencion_medica/crear/', AtencionMedicaCreateView.as_view(), name='atencion_medica_create'),
    path('atencion_medica/editar/<int:pk>/', AtencionMedicaUpdateView.as_view(), name='atencion_medica_update'),
    path('atencion_medica/eliminar/<int:pk>/', AtencionMedicaDeleteView.as_view(), name='atencion_medica_delete'),
]
