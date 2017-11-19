from django.shortcuts import render
from django.http import HttpResponse
from stock.models import Producto, Color, TipoProducto, TipoEstampado, Talla
from django.views.generic import CreateView, ListView
from .forms import AgregarProductoForm, CrearColorForm, CrearTipoProductoForm, CrearTipoEstampadoForm, CrearTallaForm

def index(request):
	lista_productos = Producto.objects.all()
	stock_camisetas = 0
	stocK_gorras = 0
	for producto in lista_productos:
		if producto.tipo_producto.codigo == "CM":
			stock_camisetas = stock_camisetas + producto.cantidad
		elif producto.tipo_producto.codigo == "GR":
			stocK_gorras = stocK_gorras + producto.cantidad
	return HttpResponse("camisteas: " + str(stock_camisetas) + " - gorras: " + str(stocK_gorras))


class AgregarProductoView(CreateView):
    model = Producto
    template_name = "agregar_producto.html"
    form_class = AgregarProductoForm

    def get_success_url(self):
        return '/stock/inventario/'


class ListaProductosView(ListView):
    model = Producto
    template_name = 'lista_productos.html'

class CrearColorView(CreateView):
    model = Color
    template_name = "crear_color.html"
    form_class = CrearColorForm

    def get_success_url(self):
        return '/stock/lista-colores/'


class ListaColoresView(ListView):
    model = Color
    template_name = 'lista_colores.html'


class CrearTipoProductoView(CreateView):
    model = TipoProducto
    template_name = "crear_tipo_producto.html"
    form_class = CrearTipoProductoForm

    def get_success_url(self):
        return '/stock/lista-tipos-productos/'


class ListaTiposProductosView(ListView):
    model = TipoProducto
    template_name = 'lista_tipos_productos.html'


class CrearTipoEstampadoView(CreateView):
    model = TipoEstampado
    template_name = "crear_tipo_estampado.html"
    form_class = CrearTipoEstampadoForm

    def get_success_url(self):
        return '/stock/lista-tipos-estampados/'


class ListaTiposEstampadosView(ListView):
    model = TipoEstampado
    template_name = 'lista_tipos_estampados.html'


class CrearTallaView(CreateView):
    model = Talla
    template_name = "crear_talla.html"
    form_class = CrearTallaForm

    def get_success_url(self):
        return '/stock/lista-tallas/'


class ListaTallasView(ListView):
    model = Talla
    template_name = 'lista_tallas.html'
