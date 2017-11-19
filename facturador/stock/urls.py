from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import AgregarProductoView, ListaColoresView, CrearColorView, ListaTiposProductosView, CrearTipoProductoView, ListaTiposEstampadosView, CrearTipoEstampadoView, ListaTallasView, CrearTallaView, ListaProductosView
from . import views

urlpatterns = [
    url(r'^inventario/$', views.index, name='index'),

    #Productos
    url(r'^agregar-producto/$', login_required(AgregarProductoView.as_view()), name='agregar_producto'),
    url(r'^lista-productos/$', login_required(ListaProductosView.as_view()), name='lista_productos'),
    
    #Colores
    url(r'^lista-colores/$', login_required(ListaColoresView.as_view()), name='lista_colores'),
    url(r'^crear-color/$', login_required(CrearColorView.as_view()), name='crear_color'),
    
    #Tipos Productos
    url(r'^lista-tipos-productos/$', login_required(ListaTiposProductosView.as_view()), name='lista_tipos_productos'),
    url(r'^crear-tipo-producto/$', login_required(CrearTipoProductoView.as_view()), name='crear_tipo_producto'),
    
    #Tipos Estampados
    url(r'^lista-tipos-estampados/$', login_required(ListaTiposEstampadosView.as_view()), name='lista_tipos_estampados'),
    url(r'^crear-tipo-estampado/$', login_required(CrearTipoEstampadoView.as_view()), name='crear_tipo_estampado'),
    
    #Tallas
    url(r'^lista-tallas/$', login_required(ListaTallasView.as_view()), name='lista_tallas'),
    url(r'^crear-talla/$', login_required(CrearTallaView.as_view()), name='crear_talla'),
    
]
