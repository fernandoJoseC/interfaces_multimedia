from rest_framework import serializers
from .models import Emprendimiento

class EmprendimientoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Emprendimiento
        fields = '__all__'