from django.db import models
from django.urls import reverse

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    descripcion = models.TextField(verbose_name="Descripción", blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock disponible", default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    activo = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('producto_detalle', kwargs={'pk': self.pk})


# Modelo Cliente
class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True, verbose_name="RUT")
    nombre = models.CharField(max_length=200, verbose_name="Nombre", blank=True)
    email = models.EmailField(verbose_name="Email", blank=True)
    habitual = models.BooleanField(default=False, verbose_name="Cliente habitual")

    def __str__(self):
        return f"{self.rut} - {self.nombre if self.nombre else 'No registrado'}"


# Modelo Venta
class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="ventas")
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True, related_name="ventas")
    rut_cliente = models.CharField(max_length=12, verbose_name="RUT Cliente")
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad vendida")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de venta")

    def __str__(self):
        return f"Venta de {self.cantidad} x {self.producto.nombre} a {self.rut_cliente} en {self.fecha.strftime('%Y-%m-%d %H:%M')}"