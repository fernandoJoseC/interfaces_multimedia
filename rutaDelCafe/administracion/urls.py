from django.urls import path
from .views import *

app_name = 'administracion'

urlpatterns = [
    #rutas del backend de la aplicacion
    path('index', Index.as_view(), name="index"),

    #rutas del rest api
    path('api/emprendimientos', Emprendimiento_APIView.as_view(),name = 'lista_emprendimientos'),
    path('api/emprendimientos/<int:id_emprendimiento>', Emprendimiento_APIView_Detalles.as_view(),name = 'detalle_emprendimientos'),
]