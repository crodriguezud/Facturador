from django import forms
from django.forms import ModelForm
from .models import TipoProducto, TipoEstampado, Talla, Color, Producto
from django.contrib.auth.models import User


class CrearColorForm(ModelForm):
    
    class Meta:
        model = Color
        fields = ['nombre','codigo'] 


class CrearTipoProductoForm(ModelForm):

    class Meta:
        model = TipoProducto
        fields = ['nombre', 'codigo']


class CrearTipoEstampadoForm(ModelForm):
    
    class Meta:
        model = TipoEstampado
        fields = ['nombre', 'codigo']


class CrearTallaForm(ModelForm):
    
    class Meta:
        model = Talla
        fields = ['nombre', 'codigo']


class AgregarProductoForm(ModelForm):

    class Meta:
        model = Producto

        fields = ('tipo_producto', 'tipo_estampado', 'talla', 'cantidad', 'descripcion', 'color',)
