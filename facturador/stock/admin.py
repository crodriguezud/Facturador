from django.contrib import admin

from .models import TipoProducto, TipoEstampado, Color, Producto, Talla

admin.site.register(TipoProducto)
admin.site.register(TipoEstampado)
admin.site.register(Talla)
admin.site.register(Color)
admin.site.register(Producto)