from django.db import models


class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class EspecialidadMedica(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Doctor(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    especialidad = models.ForeignKey(EspecialidadMedica, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"
        ordering = ['apellidos', 'nombres']


class Empleado(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class TipoSangre(models.Model):
    tipo = models.CharField(max_length=5)  # Ejemplo: A+, O-, etc.

    def __str__(self):
        return self.tipo


class Paciente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    tipo_sangre = models.ForeignKey(TipoSangre, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class MarcaMedicamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class TipoMedicamento(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre


class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(MarcaMedicamento, on_delete=models.SET_NULL, null=True)
    tipo = models.ForeignKey(TipoMedicamento, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre


class TipoGasto(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre


class GastoMensual(models.Model):
    tipo = models.ForeignKey(TipoGasto, on_delete=models.CASCADE)
    descripcion = models.TextField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.tipo.nombre} - {self.fecha} - ${self.monto}"


class Diagnostico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"




    def __str__(self):
        return f"Foto de {self.paciente} - {self.fecha.strftime('%Y-%m-%d')}"



    
class FotoPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='fotos')
    imagen = models.ImageField(upload_to='fotos_pacientes/')
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Foto de {self.paciente} - {self.fecha}"
    
    
    