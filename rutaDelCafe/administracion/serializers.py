from rest_framework import serializers
from .models import Emprendimiento, Servicios, Multimedia, Productos, Persona, Cliente, Administrador, Emprendedor, Reservas

class EmprendimientoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Emprendimiento
        fields = '__all__'

class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = '__all__'

class MultimediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multimedia
        fields = '__all__'

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model =Administrador
        fields = '__all__'

class EmprendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprendedor
        fields = '__all__'

class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = '__all__'