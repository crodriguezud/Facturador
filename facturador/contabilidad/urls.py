from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import CrearFacturaView

urlpatterns = [
    url(r'^crear-factura/$', login_required(CrearFacturaView.as_view()), name='crear_factura'),
]
