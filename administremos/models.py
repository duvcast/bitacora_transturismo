from django.db import models


class Bus(models.Model):
    """
    Modelo Bus
    """
    id_activo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200, null=True)
    codigo = models.CharField(max_length=100, null=True)
    placa = models.CharField(max_length=100, null=True)
    marca = models.CharField(max_length=100, null=True)
    modelo = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = 'bus'

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Empleado(models.Model):
    """ Modelo del empleado """
    nombre = models.CharField(max_length=200, null=True)
    codigo = models.CharField(max_length=100, null=True)
    id_empleado = models.CharField(max_length=50, null=True)
    nro_identificacion = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = 'driver'

    def __str__(self):
        return self.nombre


class BusDriver(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, verbose_name="bus")
    driver = models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="empleado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = "bus_driver"

    def __str__(self):
        return f"{self.bus} - {self.driver}"


class Relief(models.Model):
    driver = models.OneToOneField(BusDriver, on_delete=models.CASCADE, verbose_name="driver")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = "relief"

    def __str__(self):
        return self.driver


class ModosDeteccion(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    codigo = models.CharField(max_length=100, null=True)
    id_modo_deteccion = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = 'modo_deteccion'


class VariablesControl(models.Model):
    """ Modelo de Variable Control"""
    nombre = models.CharField(max_length=200, null=True)
    codigo = models.CharField(max_length=100, null=True)
    id_variable_control = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = 'variables_control'


class Sintomas(models.Model):
    """Modelo de Sintomas"""
    nombre = models.CharField(max_length=200, null=True)
    codigo = models.CharField(max_length=100, null=True)
    id_sintoma = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = 'sintomas'


class LugaresOperacion(models.Model):
    """Modelo lugar de operacion"""
    nombre = models.CharField(max_length=200, null=True)
    codigo = models.CharField(max_length=100, null=True)
    id_lugar_operacion = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = 'lugares_operacion'
