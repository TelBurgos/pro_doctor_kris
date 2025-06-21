from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from applications.doctor.forms.horariosAtencion import HorariosAtencionForm
from applications.doctor.models import HorariosAtencion  # Replace with your actual model
from applications.security.components.mixin_crud import PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin

class HorariosAtencionListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'doctor/horarios_atencion/list.html'
    model = HorariosAtencion
    context_object_name = 'horarios_atencion'
    permission_required = 'view_horariosatencion'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1 is not None:
            # Buscar por nombre del paciente o doctor usando las relaciones
            self.query.add(
                Q(doctor__nombres__icontains=q1) | 
                Q(doctor__apellidos__icontains=q1), 
                Q.OR
            )
        return self.model.objects.select_related( 'doctor').filter(self.query).order_by('fecha', 'hora')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('doctor:horariosatencion_create')
        return context
    
class HorariosAtencionCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = HorariosAtencion
    template_name = 'doctor/horarios_atencion/form.html'
    form_class = HorariosAtencionForm  # Replace with your actual form
    success_url = reverse_lazy('doctor:horariosatencion_list')
    permission_required = 'add_horariosatencion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Horario de Atención'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        horario_atencion = self.object
        messages.success(self.request, f"Éxito al crear el horario de atención para {horario_atencion.doctor}.")
        return response
    
class HorariosAtencionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = HorariosAtencion
    template_name = 'doctor/horarios_atencion/form.html'
    form_class = HorariosAtencionForm  # Replace with your actual form
    success_url = reverse_lazy('doctor:horariosatencion_list')
    permission_required = 'change_horariosatencion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar Horario de Atención'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        horario_atencion = self.object
        messages.success(self.request, f"Éxito al actualizar el horario de atención para {horario_atencion.doctor}.")
        return response
    
class HorariosAtencionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = HorariosAtencion
    template_name = 'doctor/horarios_atencion/delete.html'
    success_url = reverse_lazy('doctor:horariosatencion_list')
    permission_required = 'delete_horariosatencion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        horario_atencion = self.object
        messages.success(self.request, f"Éxito al eliminar el horario de atención para {horario_atencion.doctor}.")
        return response