from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CrearFacturadorForm, CrearFacturaProductoForm

from .models import Factura

class CrearFacturaView(CreateView):
    model = Factura
    template_name = "crear_factura.html"
    form_class = CrearFacturadorForm

    def get_success_url(self):
        return '/'
