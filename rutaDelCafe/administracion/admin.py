from django.contrib import admin
from .models import Emprendimiento, Cliente, Administrador, Emprendedor, Servicios, Reservas, Persona

# Register your models here.

admin.site.register(Emprendedor)
admin.site.register(Persona)
admin.site.register(Cliente)
admin.site.register(Administrador)
admin.site.register(Emprendimiento)
admin.site.register(Servicios)
admin.site.register(Reservas)



