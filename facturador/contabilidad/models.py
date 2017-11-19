from __future__ import unicode_literals

from django.db import models
from datetime import datetime

from django.template.defaultfilters import slugify

from stock.models import Producto
from usuario.models import Cliente, Usuario

# Create your models here.

class Factura(models.Model):
	consecutivo = models.CharField(max_length=10)
	consecutivo_slug = models.SlugField(max_length=10, blank=True, null=True)
	cliente = models.ForeignKey(Cliente)
	usuario_creacion = models.ForeignKey(Usuario)
	fecha_creacion = models.DateField(default=datetime.now, blank=True)
	estado = models.IntegerField(choices=(
		(1, "No paga"),
		(2, "Paga"),
		(3, "Anulada/Cancelada"),
		(4, "Abonó")),
		default=1)
	#usuario_actualizacion = foreignKey(Usuario)
	fecha_actualizacion = models.DateField()
	iva = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		self.consecutivo_slug = slugify(self.consecutivo)
		if self.estado in (4,2):
			for factura_producto in self.get_factura_producto():
				prod = Producto.objects.filter(pk=factura_producto.producto.pk)[0]
				prod.cantidad = prod.cantidad - factura_producto.unidades
				prod.save()
		super(self.__class__, self).save(*args, **kwargs)

	def __unicode__(self):
		return str(self.consecutivo)

	def get_factura_producto(self):
		return FacturaProducto.objects.filter(factura = self)


class FacturaProducto(models.Model):
	factura = models.ForeignKey(Factura)
	producto = models.ForeignKey(Producto)
	unidades = models.IntegerField()
	valor_producto_unidad = models.CharField(max_length=20)

	def __unicode__(self):
		return str(self.factura.consecutivo + " - " + self.valor_producto_unidad)


	