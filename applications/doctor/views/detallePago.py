from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from applications.doctor.forms.detallePago import DetallePagoForm
from applications.doctor.models import DetallePago
from applications.security.components.mixin_crud import PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin

class detallePagoListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'doctor/detalle_pago/list.html'
    model = DetallePago
    context_object_name = 'detalle_pagos'
    permission_required = 'view_detallepago'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1 is not None:
            self.query.add(Q(paciente__icontains=q1) | Q(doctor__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('fecha_pago')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('doctor:detallepago_create')
        return context
    
class detallePagoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = DetallePago
    template_name = 'doctor/detalle_pago/form.html'
    form_class = DetallePagoForm
    success_url = reverse_lazy('doctor:detallepago_list')
    permission_required = 'add_detallepago'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Detalle de Pago'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        detalle_pago = self.object
        messages.success(self.request, f"Éxito al crear el detalle de pago para {detalle_pago.paciente}.")
        return response
    
class detallePagoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = DetallePago
    template_name = 'doctor/detalle_pago/form.html'
    form_class = DetallePagoForm
    success_url = reverse_lazy('doctor:detallepago_list')
    permission_required = 'change_detallepago'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Detalle de Pago'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        detalle_pago = self.object
        messages.success(self.request, f"Éxito al actualizar el detalle de pago para {detalle_pago.paciente}.")
        return response
    
class detallePagoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = DetallePago
    template_name = 'doctor/detalle_pago/delete.html'
    success_url = reverse_lazy('doctor:detallepago_list')
    permission_required = 'delete_detallepago'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        detalle_pago = self.object
        messages.success(self.request, f"Éxito al eliminar el detalle de pago para {detalle_pago.paciente}.")
        return response