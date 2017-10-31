from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _

class Usuario(models.Model):
	usuario = models.OneToOneField(User)
	descripcion = models.TextField(blank=True, null=True)

	class Meta:
		verbose_name = _('Usuario')
		verbose_name_plural = _('Usuarios')
	
	def __unicode__(self):
		return str(self.usuario)

class Cliente(models.Model):
	nombres = models.CharField(max_length=40)
	apellidos = models.CharField(max_length=40)
	identificacion = models.CharField(max_length=15, blank=True, null=True)
	telefono = models.CharField(max_length=15, blank=True, null=True)
	correo = models.EmailField(blank=True, null=True)
	direccion = models.CharField(max_length=50, blank=True, null=True)

	def __unicode__(self):
		return str(self.nombres + " " + self.apellidos + " - " + self.identificacion)
