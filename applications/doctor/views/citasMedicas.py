from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from applications.doctor.forms.atencionMedica import AtencionMedicaForm
from applications.doctor.models import CitasMedicas
from applications.security.components.mixin_crud import PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin

class CitasMedicasListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'doctor/citas_medicas/list.html'
    model = CitasMedicas
    context_object_name = 'citas_medicas'
    permission_required = 'view_citasmedicas'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1 is not None:
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
        context['create_url'] = reverse_lazy('doctor:citasmedicas_create')
        return context
    
class CitasMedicasCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = CitasMedicas
    template_name = 'doctor/citas_medicas/form.html'
    form_class = AtencionMedicaForm
    success_url = reverse_lazy('doctor:citasmedicas_list')
    permission_required = 'add_citasmedicas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Cita Médica'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        cita_medica = self.object
        messages.success(self.request, f"Éxito al crear la cita médica para {cita_medica.paciente}.")
        return response
    
class CitasMedicasUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = CitasMedicas
    template_name = 'doctor/citas_medicas/form.html'
    form_class = AtencionMedicaForm
    success_url = reverse_lazy('doctor:citasmedicas_list')
    permission_required = 'change_citasmedicas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar Cita Médica'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        cita_medica = self.object
        messages.success(self.request, f"Éxito al actualizar la cita médica para {cita_medica.paciente}.")
        return response


class CitasMedicasDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = CitasMedicas
    template_name = 'doctor/citas_medicas/confirm_delete.html'
    success_url = reverse_lazy('doctor:citasmedicas_list')
    permission_required = 'delete_citasmedicas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_name'] = self.object.paciente
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        cita_medica = self.object
        messages.success(self.request, f"Éxito al eliminar la cita médica para {cita_medica.paciente}.")
        return response