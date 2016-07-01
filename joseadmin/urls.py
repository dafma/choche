__author__ = 'mrk2'
from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import ReservacionList, ClientesList, PaqueteList, PaqueteCreation,\
    PaqueteUpdate,PaqueteDelete, ReservacionUpdate

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^$', 'app.views.index', name='home'),
    url(r'^reservaciones/$', ReservacionList.as_view(), name='reservaciones'),
    url(r'^clientes/$', ClientesList.as_view(), name='clientes'),
    url(r'^paquete/$', PaqueteList.as_view(), name='paquetes'),


    # crud paquete
    url(r'^nuevo_paquete$', PaqueteCreation.as_view(), name='paqueteNew'),
    url(r'^editar_paquete/(?P<pk>\d+)$', PaqueteUpdate.as_view(), name='paqueteEdit'),
    url(r'^eliminar_paquete/(?P<pk>\d+)$', PaqueteDelete.as_view(), name='paqueteDelete'),

    # crud reservacion
    url(r'^editar_confirmacion/(?P<pk>\d+)$', ReservacionUpdate.as_view(), name='reservacionEdit'),



]
