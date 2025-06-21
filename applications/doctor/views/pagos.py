from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from applications.doctor.forms.pagos import PagosForm
from applications.doctor.models import Pagos
from applications.security.components.mixin_crud import PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
class PagosListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'doctor/pagos/list.html'
    model = Pagos
    context_object_name = 'pagos_list'
    permission_required = 'view_pagos'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1 is not None:
            # Buscar por nombre del paciente o doctor usando las relaciones
            self.query.add(
                Q(paciente__nombres__icontains=q1) | 
                Q(paciente__apellidos__icontains=q1) |
                Q.OR
            )
        return self.model.objects.select_related('paciente').filter(self.query).order_by('fecha', 'hora')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('doctor:pagos_create')
        return context
    
class PagosCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Pagos
    template_name = 'doctor/pagos/form.html'
    form_class = PagosForm
    success_url = reverse_lazy('doctor:pagos_list')
    permission_required = 'add_pagos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Pago'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        pago = self.object
        messages.success(self.request, f"Éxito al crear el pago para {pago.paciente}.")
        return response
    
class PagosUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Pagos
    template_name = 'doctor/pagos/form.html'
    form_class = PagosForm
    success_url = reverse_lazy('doctor:pagos_list')
    permission_required = 'change_pagos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Pago'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        pago = self.object
        messages.success(self.request, f"Éxito al actualizar el pago para {pago.paciente}.")
        return response
class PagosDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Pagos
    template_name = 'doctor/pagos/delete.html'
    success_url = reverse_lazy('doctor:pagos_list')
    permission_required = 'delete_pagos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        pago = self.object
        messages.success(self.request, f"Éxito al eliminar el pago para {pago.paciente}.")
        return response