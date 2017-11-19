from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

# Configuration API Router
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'artists', ArtistViewSet)
#router.register(r'albums', AlbumViewSet)
#router.register(r'songs', SongViewSet)

urlpatterns = [
    url(r'^', include('index.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^api/', include(router.urls)),

    # AUTH
    url(r'^cuenta/', include('allauth.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),

    # Apps
    url(r'^usuario/', include('usuario.urls')),
    url(r'^stock/', include('stock.urls')),
    url(r'^contabilidad/', include('contabilidad.urls')),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
