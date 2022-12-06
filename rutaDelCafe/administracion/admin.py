from django.contrib import admin
from .models import Emprendimiento, Cliente, Administrador, Emprendedor, Servicios, Reservas, Persona, Productos, Multimedia

class EmprendedorAdmin(admin.ModelAdmin):
    list_display = ('cedula','nombre','apellido',)
    search_fields = ('cedula','nombre', 'apellido', )
    list_filter = ('cedula',)
    ordering = ('cedula', 'nombre','apellido',)
    fieldsets =(

        ('Informacion Personal', {
            'fields': ('nombre', 'apellido','tipoDocumento' 'cedula','origin',)
        }),
        ('Informacion de contacto', {
            'fields': ('celular', 'dirrecion','correo',)
        }),
        ('Informacion de Emprendimientos', {
            'fields': ('emprendimiento',)
        }),
    )

class EmprendimientoAdmin(admin.ModelAdmin):
    list_display = ('ruc','nombreEmprendimiento',)
    search_fields = ('ruc','nombreEmprendimiento', )
    list_filter = ('ruc',)
    ordering = ('ruc','nombreEmprendimiento',)
    fieldsets =(

        ('Informacion sobre la empresa', {
            'fields': ('ruc', 'nombreEmprendimiento','descripcion' ,'servicio','video','foto')
        }),
        ('Informacion de ubicacion', {
            'fields': ('direccion', 'latitud','altitud',)
        }),
        ('Informacion de contacto ', {
            'fields': ('telFijo', 'telCelular',)
        }),
        ('Horarios de atencion', {
            'fields': ('horaApertura', 'horaCierre',)
        }),
        ('Redes Sociales', {
            'fields': ('instagram', 'facebook',)
        }),
    )

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cedula','nombre','apellido',)
    search_fields = ('cedula','nombre', 'apellido', )
    list_filter = ('cedula',)
    ordering = ('cedula','apellido', 'nombre',)
    fieldsets =(

        ('Informacion Personal', {
            'fields': ('nombre', 'apellido','tipoDocumento' 'cedula','origin',)
        }),
        ('Informacion de contacto', {
            'fields': ('celular', 'dirrecion','correo','direccion')
        }),
    )

class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('cedula','nombre','apellido',)
    search_fields = ('cedula','nombre', 'apellido', )
    list_filter = ('cedula',)
    ordering = ('cedula','apellido', 'nombre',)
    fieldsets =(

        ('Informacion Personal', {
            'fields': ('nombre', 'apellido','tipoDocumento' 'cedula','origin','usuario')
        }),
        ('Informacion de contacto', {
            'fields': ('celular', 'dirrecion','correo',)
        }),
        ('Permisos', {
            'fields': ('estado', '','rol','fechaInicio','fechaActualizacion')
        }),    
    
    )

# Register your models here.

admin.site.register(Emprendedor)
admin.site.register(Persona)
admin.site.register(Cliente)
admin.site.register(Administrador)
admin.site.register(Emprendimiento)
admin.site.register(Servicios)
admin.site.register(Reservas)
admin.site.register(Productos)
admin.site.register(Multimedia)