from django.shortcuts import render
from django.http import Http404

# Create your views here.

#primero programamos el acceso al framework a traves del restapi
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

#importamos los datos del archivo serializers
from .serializers import EmprendimientoSerializers

#importmos el modelo
from .models import Emprendimiento

#agregamos las vistas que van a influir en la presentación
from django.views import View

class Index(View):
    def get(self, request):
        #crear clase 
        empremdimentos = Emprendimiento.objects.all()
        #nombre_emprendientos = Emprendimiento.nombreEmprendiento
        #print(categorias)
        return render(request, 'presentacion/index.html', {'emprendimientos':empremdimentos} )#, {'nombreEmprendientos':nombre_emprendientos})



class Emprendimiento_APIView(APIView):

    #metodo get
    def get(self, request, format=None, *args, **kwargs): #ojo la k 
        emprendimientos = Emprendimiento.objects.all()
        serializer = EmprendimientoSerializers(emprendimientos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmprendimientoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            
class Emprendimiento_APIView_Detalles(APIView):
    #obtener todos los objetos
    def get_objeto(self, emprendimiento_id):
        try:
            return Emprendimiento.objects.get(id=emprendimiento_id)
        except Emprendimiento.DoesNotExist:
            raise Http404

    def get(self, request, id_emprendimiento, format=None):
        emprendimiento = self.get_objeto(id_emprendimiento)
        serializer = EmprendimientoSerializers(emprendimiento)
        return Response(serializer.data)

    #metodo put
    def put(self, request, id_emprendimiento, format=None):
        emprendimiento = self.get_objeto(id_emprendimiento)
        serializer = EmprendimientoSerializers(emprendimiento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)