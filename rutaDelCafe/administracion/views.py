from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

# Create your views here.

#primero programamos el acceso al framework a traves del restapi
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .forms import *

#importamos los datos del archivo serializers
from .serializers import EmprendimientoSerializers, ServiciosSerializer, MultimediaSerializer, ProductosSerializer, PersonaSerializer, ClienteSerializer, AdministradorSerializer, EmprendedorSerializer, ReservasSerializer

#importmos el modelo
from .models import Emprendimiento, Servicios, Multimedia, Productos, Persona, Cliente, Administrador, Emprendedor, Reservas

#agregamos las vistas que van a influir en la presentación
from django.views import View

#agregamos la importacion del formulario
from .forms import reservasForm

class Index(View):
    def get(self,request):
        #servicios=Servicios.objects.all()
        categorias = Emprendimiento.categoria
        #print(servicios)
        valor=[]
        for categoria in categorias:
            emprendimientos= Emprendimiento.objects.all().filter(categoria=categoria)
            valor.append(emprendimientos)
        return render(request, 'presentacion/index.html', {'categorias':categorias,'emprendimientos':emprendimientos,'valor':valor} )

class GenerarReserva(View):
    def get(self, request):
        return render(request, 'reservas/reserva.html', { })

class ListarEmprendimientos(View):
    def get (self,request, id_categoria):
        #servicios= Servicios.tipoServicio
        categorias = Emprendimiento.categoria
        if not id_categoria:
            id_categoria=1
        emprendimientos=Emprendimiento.objects.all().order_by('categoria')
        print(emprendimientos)
        return render(request, 'emprendimiento/listaEmprendimientos.html',{'emprendimientos':emprendimientos,'categorias':categorias,} )

class VerEmprendimiento(View):
    def get(self, request, idEmprendimiento):
        emprendimiento=Emprendimiento.objects.all().filter(id=idEmprendimiento)
        form=reservasForm()
        emprendimiento=emprendimiento
        return render(request,'emprendimiento/emprendimiento.html',{'form':form ,'emprendimiento':emprendimiento})

    def post(self, request, *args, **kwargs):
        form = reservaFormulario(request.POST or None, request.FILES or None)
        valor= kwargs
        if form.is_valid():
            fechaReserva= form.cleaned_data['fechaReserva']
            emprendimiento= form.cleaned_data['emprendimiento']
            cantidad=form.cleaned_data['cantidad']
            valor= form.cleaned_data['valor']
            #productos=form.cleaned_data['productos']
            reserva= Reservas(
                fechaReserva=fechaReserva,
                emprendimiento=emprendimiento,
                cantidad=cantidad,
                valor=valor
            )
            reserva.save()
            form=reservaFormulario()
            return HttpResponseRedirect("index")
        else:
            return render(request,'emprendimiento/emprendimiento.html',{'form':form})


class emprendimientoIndex(View):
    def get(self, request):
        context ={}
        context['form']= reservasForm()
        
        #crear clase
        return render(request, 'emprendimiento/emprendimiento_index.html', context)
    def post(request):
        #metodo para grabar la informacion en la BD
        pass

class ListarServicios(View):
    def get (self,request):
        servicios= Servicios.objects.all().order_by('tip')
        return render(request, 'servicio/listarServicios.html',{'servicios':servicios})

class VerCategoria(View):
    def get(self, request, idCategoria):
        categoria=Emprendimiento.objects.all().filter(id=idCategoria)
        #servicio= Servicios.objects.all().filter(id=idCategoria)

        return render(request,'servicio/servicio.html',{'categoria':categoria})

class generarReservas(View):
    pass

#-------------API VIEWS-------------

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

class Emprendedor_APIView(APIView):
    def get(self, request,format =None, *args, **Kwargs):
        emprendedores= Emprendedor.objects.all()
        serializer= EmprendedorSerializer(emprendedores,many=True)    
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=EmprendedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)    

class Emprendedor_APIView_Detalles(APIView):
    def get_object(self, emprendedor_id):
        try:
            return Emprendedor.objects.get(id=emprendedor_id)
        except Emprendedor.DoesNotExist:
            raise Http404

    def get(self,request,id_emprendedor,format=None):
        emprendedor = self.get_object(id_emprendedor)
        serializer= EmprendedorSerializer(emprendedor)
        return Response(serializer.data)

    def put(self,request,id_emprendedor, format=None):
        emprendedor=self.get_object(id_emprendedor)
        serializer= EmprendedorSerializer(emprendedor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Servicio_APIView(APIView):
    def get(self, request,format =None, *args, **Kwargs):
        servicio= Servicios.objects.all()
        serializer= ServiciosSerializer(servicio,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=ServiciosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)    

class Servicio_APIView_Detalles(APIView):

    def get_object(self, servicio_id):
        try:
            return Servicios.objects.get(id=servicio_id)
        except Servicios.DoesNotExist:
            raise Http404

    def get(self,request,id_servicio,format=None):
        servicio = self.get_object(id_servicio)
        serializer= ServiciosSerializer(servicio)
        return Response(serializer.data)

    def put(self,request,id_servicio, format=None):
        servicio=self.get_object(id_servicio)
        serializer= ServiciosSerializer(servicio,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)