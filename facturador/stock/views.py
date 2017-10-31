from django.shortcuts import render
from django.http import HttpResponse
from stock.models import Producto

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