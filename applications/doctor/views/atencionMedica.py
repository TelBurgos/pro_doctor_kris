from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from applications.doctor.forms.atencionMedica import AtencionMedicaForm
from applications.doctor.models import AtencionMedica
from applications.security.components.mixin_crud import PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin

class AtencionMedicaListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'doctor/AtencionMedica/list.html'
    model = AtencionMedica
    context_object_name = 'atenciones_medicas'
    permission_required = 'view_atencionmedica'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1 is not None:
            # Buscar por nombre del paciente o doctor usando las relaciones
            self.query.add(
                Q(paciente__nombres__icontains=q1) | 
                Q(paciente__apellidos__icontains=q1) |
                Q(doctor__nombres__icontains=q1) | 
                Q(doctor__apellidos__icontains=q1), 
                Q.OR
            )
        return self.model.objects.select_related('paciente', 'doctor').filter(self.query).order_by('fecha', 'hora')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('doctor:atencionmedica_create')
        return context
    
class AtencionMedicaCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = AtencionMedica
    template_name = 'doctor/AtencionMedica/form.html'
    form_class = AtencionMedicaForm
    success_url = reverse_lazy('doctor:atencionmedica_list')
    permission_required = 'add_atencionmedica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Atención Médica'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        atencion_medica = self.object
        messages.success(self.request, f"Éxito al crear la atención médica para {atencion_medica.paciente}.")
        return response

class AtencionMedicaUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = AtencionMedica
    template_name = 'doctor/AtencionMedica/form.html'
    form_class = AtencionMedicaForm
    success_url = reverse_lazy('doctor:atencionmedica_list')
    permission_required = 'change_atencionmedica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar Atención Médica'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        atencion_medica = self.object
        messages.success(self.request, f"Éxito al actualizar la atención médica para {atencion_medica.paciente}.")
        return response
    
class AtencionMedicaDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = AtencionMedica
    template_name = 'doctor/AtencionMedica/delete.html'
    success_url = reverse_lazy('doctor:atencionmedica_list')
    permission_required = 'delete_atencionmedica'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = self.success_url
        return context
    def form_valid(self, form):
        response = super().form_valid(form)
        atencion_medica = self.object
        messages.success(self.request, f"Éxito al eliminar la atención médica para {atencion_medica.paciente}.")
        return response

