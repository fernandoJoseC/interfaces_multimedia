from django.urls import path
from .views import *

app_name = 'administracion'

urlpatterns = [
    path("emprendimientos", Emprendimiento_APIView.as_view(),name='listaemprendimientos'),
    path("emprendimientos/<int:id_emprendimiento>", Emprendimiento_APIView_Detalles.as_view(),name ='detalleEmprendimientos'),
    path('emprendimientos/listado/<int:id_servicio>',ListarEmprendimientos.as_view(),name='listadoEmprendimientos' ),
    path("emprendedores",Emprendedor_APIView.as_view(),name="listaEmprendedores"),
    path("emprendedores/<int:id_emprendedor>", Emprendedor_APIView_Detalles.as_view(),name ='detalleEmprendedores'),
    path('reservas/reserva',GenerarReserva.as_view(),name='reserva' ),
    path('index', Index.as_view(), name="index"),
    path("servicios", Servicio_APIView.as_view(),name='listaServicios'),
    path("servicios/<int:id_servicio>",Servicio_APIView_Detalles.as_view(),name ='detalleServicios'),
    path('servicios/listado/<int:id_servicio>',ListarServicios.as_view(),name='listadoServicios' ),
]