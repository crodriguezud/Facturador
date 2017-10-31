from django.contrib import admin

from .models import Factura, FacturaProducto

admin.site.register(Factura)
admin.site.register(FacturaProducto)