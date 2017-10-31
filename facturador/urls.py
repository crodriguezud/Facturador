from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^usuario/', include('usuario.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^stock/', include('stock.urls')),
]