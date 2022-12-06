from django.db import models
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.db.models.deletion import CASCADE
# Create your models here.

# Usaremos el diagrama de clases

class Rol(models.Model):

    nombre = models.CharField(verbose_name='Ingresar el nombre del rol', max_length=80, help_text='Ingrese el nombre del rol')
    descripcion = models.TextField(verbose_name='Ingrese una descrición detallada del rol', help_text='Descripcion del rol')

    class Meta:
        verbose_name = 'Permiso del sistema'
        verbose_name_plural = 'Permisos para usuarios'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        permisos_defecto = ['add', 'change', 'delete', 'view']
        if not self.id:
            nuevo_grupo, creado = Group.objects.get_or_create(name=f'{self.nombre}')
            for permiso_temp in permisos_defecto:
                permiso, creado = Permission.objects.update_or_create(
                    name = f'Can {permiso_temp} {self.nombre} ',
                    content_type = ContentType.objects.get_for_model(Rol),
                    codename = f'{permiso_temp}_{self.nombre}'
                )
                if creado:
                    nuevo_grupo.permissions.add(permiso.id)
            super().save(*args, **kwargs)
        else:
            rol_antiguo = Rol.objects.filter(id=self.id).values('nombre').first()
            if rol_antiguo['nombre'] == self.nombre:
                super().save(*args, **kwargs)
            else:
                Group.objects.filter(name=rol_antiguo['nombre'].update(name=f'{self.nombre}'))
                for permiso_temp in permisos_defecto:
                    Permission.objects.filter(codename=f"{permiso_temp}_{rol_antiguo['nombre']}").update(
                        codename = f'{permiso_temp}_{self.nombre}',
                        name= f'Can {permiso_temp} {self.nombre}'
                    )
                super().save(*args, **kwargs)

class Servicios(models.Model):

    TIPOS_SERVICIO_CHOICES = [
        ('ventaProductos', 'Venta de productos'),
        ('servicioRestaurante', 'Alojamiento'),
        ('produccionProductos', 'Produccion de productos'),
        ('atractivoTuristico', 'Atractivo Turistico'),
        ('hospedaje', 'Hospedaje'),
        ('cafeteria', 'Cafeteria'),
        ('piscina', 'Piscina'),
        ('camping', 'Camping'),
        ('caminata', 'Caminata'),
        ('cabalgata', 'Cabalgata'),
        ('recreacion', 'Recreacion'),
        ('comidaTipica', 'Comida Tipica'),
        ('comidaRapida', 'Comida Rapida'),
        ('comidaCoreana', 'Comida Coreana'),
    ]

    #nombreServicio = models.CharField(verbose_name="Nombre del Servicio", max_length=500)
    tipoServicio = models.CharField(verbose_name="Tipo de servicio", max_length=20, choices=TIPOS_SERVICIO_CHOICES, null=True, blank=True)
    #precio = models.CharField(verbose_name="Precio", max_length=6, null=True, blank=True)
    descripcionServicio = models.CharField(
        verbose_name="Descripcion del Servicio", max_length=500)

class Multimedia(models.Model):
    descripcion = models.CharField(verbose_name="Descripcion", max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to="Imagenes del emprendimiento", verbose_name="Subir imagenes del emprendimiento", blank=True, null=True)
    video = models.URLField(verbose_name="video promocional", blank=True, null=True)

class Productos(models.Model):
    nombre_producto = models.CharField(verbose_name="Nombre del producto", max_length=100, null=True, blank=True)
    precio = models.CharField(verbose_name="Precio del producto unitario", max_length=5, null=True, blank=True)
    descripcion = models.CharField(verbose_name="Descripcion del producto", max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to="Imagenes del producto", verbose_name="Subir imagenes del producto", blank=True, null=True)

class Persona(models.Model):

    TIPO_DOCUMENTO_CHOICE = [
        ('cedula', 'Cedula'),
        ('pasaporte', 'Pasaporte'),
    ]

    email = models.EmailField(max_length=150, unique=True, null=True)
    tipo_documento = models.CharField(verbose_name="Tipo de documento", max_length=20, choices=TIPO_DOCUMENTO_CHOICE, null=True, blank=True)
    cedula = models.CharField(verbose_name="Cedula", max_length=13)
    firstName = models.CharField(verbose_name="Nombres", max_length=200, null=True, blank=True)
    lastName = models.CharField(verbose_name="Apellidos", max_length=200, null=True, blank=True)
    telefono = models.CharField(verbose_name="Numero de telefono", max_length=13)
    direccion = models.CharField(verbose_name="Direccion", max_length=500)
    fechaNacmiento = models.DateField(verbose_name="Fecha de Nacmiento")
    nacionalidad = models.CharField(verbose_name="Nacionalidad", max_length=50)
    foto = models.ImageField(upload_to="fotosUsuarios",
                             verbose_name="Subir su foto de usuario", blank=True, null=True)

    # metodo para presentar el objeto creado

    def __str__(self):
        return self.cedula

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

class Administrador(Persona):

    estado_Choice=[
        ('ACTIVO','Activo'),('INACTIVO','Inactivo')
    ]

    rol= models.OneToOneField(Rol,verbose_name="Rol_Administrador", on_delete=models.RESTRICT)
    usuario = models.OneToOneField(User, on_delete=CASCADE, blank=True, null=True)
    fechaInicio= models.DateTimeField(blank=True, null=True)
    fechaActualizacion = models.DateTimeField(blank=True, null=True)
    estado= models.CharField(choices=estado_Choice,max_length=20,blank=True, null=True)

class Emprendimiento(models.Model):

    TIPOS_CALIFICACION_CHOICES = [
        ('bueno', 'Bueno'),
        ('malo', 'Malo'),
        ('regular', 'Regular'),
        ('normal', 'Normal'),
        ('excelentes', 'Excelente'),
    ]

    DISPONIBILIDAD_CHOICES = [
        ('si', 'Si'),
        ('no', 'No'),
    ]

    CATEGORIAS_CHOICES = [
        ('Restaurante', 'Restaurante'),
        ('Hospedaje', 'Hospedaje'),
        ('Atraccion', 'Atraccion'),
        ('Market', 'Market'),
    ]

    nombreEmprendimiento = models.CharField(
        verbose_name="Nombre del Emprendimiento", max_length=500)
    direccionEmprendiento = models.CharField(
        verbose_name="Direccion", max_length=500)
    telCelular = models.CharField(
        verbose_name="Telefono celular", max_length=13)
    telFijo = models.CharField(verbose_name="Telefono Fijo", max_length=13)
    descripcion = models.TextField(verbose_name="Descripcion")
    horaApertura = models.DateTimeField()
    horaCierre = models.DateTimeField()
    latitud = models.CharField(verbose_name="Latitud", max_length=50, null=True, blank=True)
    altitud = models.CharField(verbose_name="Altitud", max_length=50, null=True, blank=True)
    #imagen = models.ImageField(upload_to="fotosEmprendimiento", otra clase
    multimedia = models.ManyToManyField(Multimedia)                  
    disponibilidad = models.CharField(
        verbose_name="Disponibilidad", max_length=3, choices=DISPONIBILIDAD_CHOICES, blank=True, null=True)
    calificacion = models.CharField(
        verbose_name="Calificacion", max_length=20, choices=TIPOS_CALIFICACION_CHOICES, blank=True, null=True)
    resena = models.CharField(verbose_name="Resena",
                              max_length=500, blank=True, null=True)
    servicios = models.ManyToManyField(Servicios)
    productos = models.ManyToManyField(Productos)
    categoria = models.CharField(verbose_name="Categoria", max_length=15, choices=CATEGORIAS_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.nombreEmprendimiento

    class Meta:
        verbose_name = "Emprendiento"
        verbose_name_plural = "Emprendientos"


class Cliente(Persona):

    paisOrigen = models.CharField(
        verbose_name="Pais de origen", max_length=200)


class Administrador(Persona):

    fechaInicio = models.DateTimeField(verbose_name="Fecha de inicio")
    fechaActualizacion = models.DateTimeField(
        verbose_name="Fecha de actualizacion")
    estado = models.BooleanField()

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"


class Emprendedor(Persona):

    # relacion de 1 a muchos
    emprendimientos = models.ManyToManyField(Emprendimiento, blank=True)

    class Meta:
        verbose_name = "Emprendedor"
        verbose_name_plural = "Emprendedores"


class Reservas(models.Model):
    fechaLlegada = models.DateField(verbose_name="Ingrese la fecha de llegada")
    fechaSalida = models.DateField(verbose_name="Ingrese la fecha de salida")
    numPersonas = models.IntegerField(
        verbose_name="Ingrese el numero de personas")
    descripcion = models.CharField(
        verbose_name="Alguna descripcion al momento de la reserva", max_length=500)
    # add tipo de productos a comprar para reservarlos
    productos = models.ManyToManyField(Productos)
