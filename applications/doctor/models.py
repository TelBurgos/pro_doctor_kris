from django.db import models

from applications.core.models import Paciente
from applications.core.models import Doctor      

class AtencionMedica(models.Model):
    fecha = models.DateField(verbose_name="Fecha de Atención")
    hora = models.TimeField(verbose_name="Hora de Atención")
    
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE,verbose_name="Paciente")
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,verbose_name="Doctor")
    motivo_consulta = models.TextField(verbose_name="Motivo de Consulta",null=True,blank=True)

    def __str__(self):  # corregido de _str_ a __str__
        return f"{self.fecha} - {self.paciente} - {self.doctor}"

    class Meta:
        verbose_name = "Atención Médica"
        verbose_name_plural = "Atenciones Médicas"
        ordering = ['fecha', 'hora']

class CitasMedicas(models.Model):
    fecha_cita = models.DateField(verbose_name="Fecha de Cita")
    hora_cita = models.TimeField(verbose_name="Hora de Cita",)
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE,verbose_name="Paciente")
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,verbose_name="Doctor")
    motivo_cita = models.TextField(verbose_name="Motivo de Cita", null=True, blank=True)

    def _str_(self):
        return f"{self.fecha_cita} - {self.paciente} - {self.doctor}"

    class Meta:
        verbose_name = "Cita Médica"
        verbose_name_plural = "Citas Médicas"
        ordering = ['fecha_cita', 'hora_cita']


class Pagos(models.Model):
    fecha_pago = models.DateField(verbose_name="Fecha de Pago")
    monto = models.DecimalField(verbose_name="Monto", max_digits=10, decimal_places=2)
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE,verbose_name="Paciente")
    metodo_pago = models.CharField(max_length=50, verbose_name="Método de Pago", null=True, blank=True)

    def _str_(self):
        return f"{self.fecha_pago} - {self.paciente} - {self.monto}"

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        ordering = ['fecha_pago']
        constraints = [
            models.UniqueConstraint(fields=['fecha_pago', 'paciente'], name='unique_fecha_paciente')
        ]

class DetallePago(models.Model):
    pago = models.ForeignKey(Pagos, on_delete=models.CASCADE, verbose_name="Pago", related_name="detalles")
    descripcion = models.CharField(max_length=200, verbose_name="Descripción")
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto")

    def _str_(self):
        return f"{self.pago} - {self.descripcion} - {self.monto}"

    class Meta:
        verbose_name = "Detalle de Pago"
        verbose_name_plural = "Detalles de Pago"
        ordering = ['pago', 'descripcion']

class HorariosAtencion(models.Model):
    dia_semana = models.CharField(max_length=10, verbose_name="Día de la Semana")
    hora_inicio = models.TimeField(verbose_name="Hora de Inicio")
    hora_fin = models.TimeField(verbose_name="Hora de Fin")
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,verbose_name="Doctor")

    def _str_(self):
        return f"{self.dia_semana} - {self.hora_inicio} a {self.hora_fin} - {self.doctor}"

    class Meta:
        verbose_name = "Horario de Atención"
        verbose_name_plural = "Horarios de Atención"
        ordering = ['dia_semana', 'hora_inicio']
        constraints = [
            models.UniqueConstraint(fields=['dia_semana', 'hora_inicio', 'doctor'], name='unique_horario_atencion')
        ]

class ServiciosAdicionales(models.Model):
    nombre_servicio = models.CharField(max_length=100, verbose_name="Nombre del Servicio")
    descripcion = models.TextField(verbose_name="Descripción", null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")

    def _str_(self):
        return f"{self.nombre_servicio} - {self.precio}"

    class Meta:
        verbose_name = "Servicio Adicional"
        verbose_name_plural = "Servicios Adicionales"
        ordering = ['nombre_servicio']
        constraints = [
            models.UniqueConstraint(fields=['nombre_servicio'], name='unique_nombre_servicio')
        ]