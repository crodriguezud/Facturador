from django import forms
from django.forms import ModelForm
from .models import Factura, FacturaProducto
from django.contrib.auth.models import User
from usuario.models import Cliente

class CrearFacturadorForm(ModelForm):

    class Meta:
        model = Factura
        fields = ('cliente', 'estado', 'iva',)

class CrearFacturaProductoForm(ModelForm):
    
    class Meta:
        model = FacturaProducto
        fields = ('factura', 'producto', 'unidades', 'valor_producto_unidad',)

