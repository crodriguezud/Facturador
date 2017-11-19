from __future__ import unicode_literals

from django.db import models

class TipoProducto(models.Model):
	codigo = models.CharField(max_length=5)
	nombre = models.CharField(max_length=20)

	def __str__(self):
		return str(self.nombre)

class TipoEstampado(models.Model):
	codigo = models.CharField(max_length=5)
	nombre = models.CharField(max_length=20)

	def __str__(self):
		return str(self.nombre)

class Talla(models.Model):
	codigo = models.CharField(max_length=5)
	nombre = models.CharField(max_length=20)

	def __str__(self):
		return str(self.nombre)

class Color(models.Model):
	codigo = models.CharField(max_length=5)
	nombre = models.CharField(max_length=20)

	def __str__(self):
		return str(self.nombre)

class Producto(models.Model):
	tipo_producto = models.ForeignKey(TipoProducto)
	tipo_estampado = models.ManyToManyField(TipoEstampado)
	talla = models.ForeignKey(Talla, blank=True, null=True)
	cantidad = models.IntegerField()
	descripcion = models.TextField(max_length=500)
	color = models.ForeignKey(Color)

	def __str__(self):
		return str(self.tipo_producto.nombre + " - " + self.color.nombre + " - " + str(self.cantidad))
