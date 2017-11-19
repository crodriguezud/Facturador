from django import forms
from django.forms import ModelForm
from .models import Factura
from django.contrib.auth.models import User
from usuario.models import Cliente

class CrearFacturadorForm(ModelForm):
    
    def init_form_data(self, user):
        self.fields['cliente'] = forms.ModelChoiceField(
            widget=forms.Select(
                attrs={
                    'class': 'datos_usuario form-control'
                }
            ),
            queryset=Cliente.objects.filter(id=user.id)
        )

    class Meta:
        model = Factura

        fields = ('cliente', 'estado', 'iva',)

    def clean(self):
        cleaned_data = super(CrearFacturadorForm, self).clean()
        cliente = cleaned_data.get("cliente")
        estado = cleaned_data.get("estado")
        iva = cleaned_data.get("iva")
        if Factura.objects.filter(cliente__id=cliente.id, estado=estado, iva=iva).first() is not None:
            raise forms.ValidationError("Se ha creado la factura %s" % nombre)
