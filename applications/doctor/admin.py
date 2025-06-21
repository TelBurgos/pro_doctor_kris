from django.contrib import admin
from applications.doctor.models import AtencionMedica, CitasMedicas, DetallePago, HorariosAtencion, Pagos, ServiciosAdicionales

@admin.register(AtencionMedica)
class AtencionMedicaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora', 'paciente', 'doctor', 'get_motivo_consulta')
    search_fields = ('paciente__nombres', 'paciente__apellidos', 'doctor__nombres', 'doctor__apellidos')
    list_filter = ('fecha', 'doctor', 'paciente')
    ordering = ('-fecha', '-hora')
    date_hierarchy = 'fecha'
    list_per_page = 25
    
    def get_motivo_consulta(self, obj):
        return obj.motivo_consulta[:50] + "..." if obj.motivo_consulta and len(obj.motivo_consulta) > 50 else obj.motivo_consulta or "Sin motivo"
    get_motivo_consulta.short_description = 'Motivo de Consulta'
    
@admin.register(CitasMedicas)
class CitasMedicasAdmin(admin.ModelAdmin):
    # Campos corregidos - usar fecha_cita y hora_cita en lugar de fecha y hora
    list_display = ('paciente', 'doctor', 'fecha_cita', 'hora_cita')
    search_fields = ('paciente', 'doctor', 'motivo_cita')  # También corregido motivo_cita
    list_filter = ('fecha_cita', 'doctor')
    ordering = ('-fecha_cita', '-hora_cita')
    date_hierarchy = 'fecha_cita'
    list_editable = ('hora_cita',)
    list_per_page = 25

@admin.register(Pagos)
class PagosAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha_pago', 'monto', 'metodo_pago')
    search_fields = ('paciente',)
    list_filter = ('fecha_pago', 'metodo_pago')
    ordering = ('-fecha_pago',)
    date_hierarchy = 'fecha_pago'
    list_per_page = 25

@admin.register(DetallePago)
class DetallePagoAdmin(admin.ModelAdmin):
    list_display = ('pago', 'descripcion', 'monto')
    search_fields = ('descripcion',)
    list_filter = ('pago__fecha_pago',)
    ordering = ('-pago__fecha_pago',)
    list_per_page = 25

@admin.register(HorariosAtencion)
class HorariosAtencionAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'dia_semana', 'hora_inicio', 'hora_fin')
    search_fields = ('doctor',)  # Corregido - doctor es CharField, no tiene 'nombres'
    list_filter = ('dia_semana', 'doctor')
    ordering = ('doctor', 'dia_semana')
    list_per_page = 25

@admin.register(ServiciosAdicionales)
class ServiciosAdicionalesAdmin(admin.ModelAdmin):
    # Campos corregidos - usar nombre_servicio y precio en lugar de nombre y costo
    list_display = ('nombre_servicio', 'descripcion', 'precio')
    search_fields = ('nombre_servicio',)
    list_filter = ('precio',)
    ordering = ('nombre_servicio',)
    list_per_page = 25