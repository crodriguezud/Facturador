from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CrearFacturadorForm

from .models import Factura

class CrearFacturaView(CreateView):
    model = Factura
    template_name = "crear_factura.html"
    form_class = CrearFacturadorForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.init_form_data(request.user)
        return self.render_to_response(self.get_context_data(form=form))
